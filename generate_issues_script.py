import requests
import time
from github import Github

REPO_JSON_URL = "https://switch.cdn.fortheusers.org/repo.json"
MY_REPO_NAME = "auggeythecat/21.0.0-Homebrew-Compatability"
GITHUB_TOKEN = "<You are not stealing my token :}>"

def main():
    if not GITHUB_TOKEN or not MY_REPO_NAME:
        print("Error: GITHUB_TOKEN or GITHUB_REPOSITORY environment variables missing.")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(MY_REPO_NAME)
    
    print(f"Fetching {REPO_JSON_URL}...")
    response = requests.get(REPO_JSON_URL)
    data = response.json()
    packages = data.get('packages', [])

    print(f"Found {len(packages)} packages. Scanning...")
    open_issues = repo.get_issues(state='open')
    existing_titles = [issue.title for issue in open_issues]

    issues_index = 2
    issues_created = 0
    
    for pkg in packages:
        # if issues_created >= 1: 
        #     print("Hit batch limit of 1 issue. Stopping for now.")
        #     break

        try:
            pkg_date_str = pkg.get('updated', '01/01/1970')
                
            issue_title = f"[Needs Update] {pkg.get('name', 'Unknown')}"

            if issue_title in existing_titles:
                issues_index += 1
                print(f"Skipping {pkg['name']} (Issue already exists)")
                continue


            folder_name = "progress/" + "".join(c for c in pkg.get('name') if c.isalnum() or c in (' ', '_', '-')).strip().replace(' ', '_')
            file_path = f"{folder_name}/NOTES.md"
            try:
                repo.get_contents(file_path)
                print(f"Folder for {folder_name} already exists.")
            except:
                folder_readme_content = (
                    f"# {pkg.get('Notes:')}\n\n"
                    f"Tracking updates for {pkg.get('name')}.\n"
                    f"Original URL: {pkg.get('url')}\n"
                )
                
                repo.create_file(
                    path=file_path,
                    message=f"Initial setup for {pkg.get('name')}",
                    content=folder_readme_content,
                    branch="main"
                )
                print(f"Created folder: /{folder_name}")

            body = (
                f"## {pkg.get('title', pkg.get('name'))}\n\n"
                f"**Author:** {pkg.get('author')}\n"
                f"**Category:** {pkg.get('category')}\n"
                f"**Source/Home:** {pkg.get('url')}\n"
                f"**Last Updated:** {pkg_date_str}\n"
                f"### Description\n"
                f"{pkg.get('description')}\n\n"
            )

            issue_body = (
                f"## Technical Details\n"
                f"Recompilation required\n"
                f"### Current Status\n"
                f"This app is currently unattempted.\n"
            )

            print(f"Creating issue for: {pkg['name']}")
            repo.create_issue(title=issue_title, body=body)
            repo.get_issue(number=issues_index).create_comment(body=issue_body)
            repo.get_issue(number=issues_index).add_to_labels("Unattempted")
            repo.get_issue(number=issues_index).add_to_labels("Needs Recompilation")
            issues_created += 1
            issues_index += 1
            
            time.sleep(5)

        except ValueError as e:
            print(f"Date parsing error for {pkg.get('name')}: {e}")
            continue

    print(f"Done. Created {issues_created} new issues.")

if __name__ == "__main__":
    main()
