import json
import os
import shutil
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GROUPS_FILE = os.path.join(BASE_DIR, "groups.json")
GROUPS_DIR = os.path.join(BASE_DIR, "Groups")
MASTER_README = os.path.join(BASE_DIR, "README.md")


# ============================================================
# BASIC HELPERS
# ============================================================

def run_git(command):
    """Run a git command safely on Windows."""
    return subprocess.run(
        command,
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )


def load_groups():
    if not os.path.exists(GROUPS_FILE):
        print("\n❌ groups.json not found.")
        return {}

    try:
        with open(GROUPS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"\n❌ groups.json is invalid:\n{e}")
        return {}


def save_groups(groups):
    with open(GROUPS_FILE, "w", encoding="utf-8") as f:
        json.dump(groups, f, indent=4, ensure_ascii=False)

    print("\n✅ groups.json updated.")


def group_folder(group_id):
    return os.path.join(GROUPS_DIR, f"Group-{int(group_id):02d}")


def get_presentation_file(folder):
    if not os.path.exists(folder):
        return None

    allowed = [".pdf", ".pptx", ".ppt"]

    for file in os.listdir(folder):
        if os.path.splitext(file)[1].lower() in allowed:
            return os.path.join(folder, file)

    return None


def press_enter():
    input("\nPress Enter to continue...")


# ============================================================
# GROUP DISPLAY
# ============================================================

def list_groups(groups):
    print("\n" + "=" * 70)
    print("PROJECT GROUPS")
    print("=" * 70)

    if not groups:
        print("No groups found.")
        return

    for group_id, data in groups.items():
        topic = data.get("topic", "No topic")
        members = data.get("members", [])

        print(f"\nGroup {int(group_id):02d}")
        print(f"  Topic   : {topic}")
        print(f"  Members : {', '.join(members) if members else 'None'}")

        github = data.get("github", "")
        if github:
            print(f"  GitHub  : {github}")
        else:
            print("  GitHub  : Not provided")


def select_group(groups):
    list_groups(groups)

    if not groups:
        return None

    group_id = input("\nEnter group number: ").strip()

    if group_id not in groups:
        print("\n❌ Group not found.")
        return None

    return group_id


# ============================================================
# VIEW GROUP
# ============================================================

def view_group(groups):
    group_id = select_group(groups)

    if group_id is None:
        return

    data = groups[group_id]
    folder = group_folder(group_id)

    print("\n" + "=" * 60)
    print(f"GROUP {int(group_id):02d}")
    print("=" * 60)

    print(f"\nTopic:")
    print(data.get("topic", "Not provided"))

    print("\nMembers:")
    for member in data.get("members", []):
        print(f"  • {member}")

    print("\nGitHub:")
    print(data.get("github") or "Not provided")

    print("\nFiles:")

    if os.path.exists(folder):
        files = os.listdir(folder)

        if files:
            for file in files:
                print(f"  • {file}")
        else:
            print("  No files.")
    else:
        print("  Group folder does not exist.")

    press_enter()


# ============================================================
# UPDATE GITHUB LINK
# ============================================================

def update_github(groups):
    group_id = select_group(groups)

    if group_id is None:
        return

    current = groups[group_id].get("github", "")

    print("\nCurrent GitHub link:")
    print(current if current else "None")

    print("\nEnter the new GitHub repository URL.")
    print("Type REMOVE if you intentionally want to remove it.")

    new_link = input("\nGitHub URL: ").strip()

    if not new_link:
        print("\n⚠️ No input provided. Existing link was kept.")
        return

    if new_link.upper() == "REMOVE":
        confirm = input(
            "Type REMOVE again to confirm deletion of the GitHub link: "
        ).strip()

        if confirm != "REMOVE":
            print("\n❌ GitHub link was not removed.")
            return

        groups[group_id]["github"] = ""
    else:
        groups[group_id]["github"] = new_link

    save_groups(groups)
    print("\n✅ GitHub link updated.")


# ============================================================
# ADD NEW GROUP
# ============================================================

def add_group(groups):
    print("\n" + "=" * 60)
    print("ADD NEW GROUP")
    print("=" * 60)

    group_numbers = [int(x) for x in groups.keys() if str(x).isdigit()]

    next_number = max(group_numbers, default=0) + 1

    print(f"\nSuggested group number: {next_number:02d}")

    custom = input(
        "Enter group number or press Enter to use suggested number: "
    ).strip()

    group_id = custom if custom else str(next_number)

    if not group_id.isdigit():
        print("\n❌ Invalid group number.")
        return

    group_id = str(int(group_id))

    if group_id in groups:
        print("\n❌ That group already exists.")
        return

    topic = input("\nProject topic: ").strip()

    if not topic:
        print("\n❌ Topic cannot be empty.")
        return

    print("\nEnter member names one by one.")
    print("Press Enter on an empty line when finished.")

    members = []

    while True:
        name = input("Member: ").strip()

        if not name:
            break

        members.append(name)

    github = input("\nGitHub repository URL (optional): ").strip()

    groups[group_id] = {
        "topic": topic,
        "members": members,
        "github": github
    }

    save_groups(groups)

    folder = group_folder(group_id)
    os.makedirs(folder, exist_ok=True)

    # Create initial README
    readme_path = os.path.join(folder, "README.md")

    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(
                f"# {topic}\n\n"
                f"## Members\n\n"
                + "\n".join(f"- {member}" for member in members)
                + "\n"
            )

    print(f"\n✅ Group {int(group_id):02d} created.")
    print(f"📁 Folder: Groups/Group-{int(group_id):02d}")


# ============================================================
# UPDATE GROUP README
# ============================================================

def update_readme(groups):
    group_id = select_group(groups)

    if group_id is None:
        return

    folder = group_folder(group_id)

    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    print("\nCurrent README:")
    print("-" * 60)

    readme_path = os.path.join(folder, "README.md")

    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                print(f.read())
        except UnicodeDecodeError:
            print("⚠️ Existing README could not be read as UTF-8.")
    else:
        print("No README exists.")

    print("-" * 60)

    source = input(
        "\nEnter the path to the new README file: "
    ).strip().strip('"')

    if not os.path.isfile(source):
        print("\n❌ File not found.")
        return

    try:
        shutil.copy2(source, readme_path)
        print("\n✅ README replaced successfully.")
    except Exception as e:
        print(f"\n❌ Failed to replace README:\n{e}")


# ============================================================
# UPDATE PRESENTATION
# ============================================================

def update_presentation(groups):
    group_id = select_group(groups)

    if group_id is None:
        return

    folder = group_folder(group_id)
    os.makedirs(folder, exist_ok=True)

    print("\nSupported presentation formats:")
    print("  PDF")
    print("  PPTX")
    print("  PPT")

    source = input(
        "\nEnter the path to the new presentation: "
    ).strip().strip('"')

    if not os.path.isfile(source):
        print("\n❌ File not found.")
        return

    extension = os.path.splitext(source)[1].lower()

    if extension not in [".pdf", ".pptx", ".ppt"]:
        print("\n❌ Unsupported presentation format.")
        print("Use .pdf, .pptx or .ppt.")
        return

    # Remove existing presentations
    for file in os.listdir(folder):
        ext = os.path.splitext(file)[1].lower()

        if ext in [".pdf", ".pptx", ".ppt"]:
            old_path = os.path.join(folder, file)

            try:
                os.remove(old_path)
                print(f"🗑️ Removed old presentation: {file}")
            except Exception as e:
                print(f"❌ Could not remove {file}: {e}")
                return

    destination = os.path.join(
        folder,
        f"Presentation{extension}"
    )

    try:
        shutil.copy2(source, destination)
        print("\n✅ Presentation replaced successfully.")
        print(f"📄 {os.path.basename(destination)}")
    except Exception as e:
        print(f"\n❌ Failed to copy presentation:\n{e}")


# ============================================================
# DELETE GROUP
# ============================================================

def delete_group(groups):
    group_id = select_group(groups)

    if group_id is None:
        return

    data = groups[group_id]

    print("\n" + "=" * 60)
    print("⚠️ DELETE GROUP")
    print("=" * 60)

    print(f"\nGroup: {int(group_id):02d}")
    print(f"Topic: {data.get('topic', 'Unknown')}")

    print("\nMembers:")
    for member in data.get("members", []):
        print(f"  • {member}")

    print("\n⚠️ This will delete:")
    print(f"  • Group {int(group_id):02d} from groups.json")
    print(f"  • Groups/Group-{int(group_id):02d}/ and everything inside it")

    print("\nThis action changes your local working directory.")
    print("It will NOT be pushed to GitHub until you commit and push.")

    confirm = input(
        "\nType DELETE to confirm: "
    ).strip()

    if confirm != "DELETE":
        print("\n❌ Deletion cancelled.")
        return

    # Remove metadata
    del groups[group_id]
    save_groups(groups)

    # Remove folder
    folder = group_folder(group_id)

    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
            print(f"🗑️ Deleted folder: Groups/Group-{int(group_id):02d}")
        except Exception as e:
            print(f"\n❌ Could not delete group folder:\n{e}")
            return

    print(f"\n✅ Group {int(group_id):02d} completely removed.")


# ============================================================
# MASTER README
# ============================================================

def generate_master_readme(groups):
    print("\nGenerating master README...")

    if not os.path.exists(MASTER_README):
        print("\n❌ README.md not found.")
        return

    try:
        with open(MASTER_README, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"\n❌ Could not read README.md:\n{e}")
        return

    start_marker = "## Project Groups"
    end_marker = "## Folder Structure"

    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1 or end <= start:
        print("\n❌ Could not find README section markers.")
        print("Expected:")
        print("  ## Project Groups")
        print("  ## Folder Structure")
        return

    rows = []

    for group_id in sorted(groups.keys(), key=lambda x: int(x)):
        data = groups[group_id]

        number = int(group_id)
        topic = data.get("topic", "Not provided")
        members = data.get("members", [])
        github = data.get("github", "")

        folder = f"Groups/Group-{number:02d}"
        readme_link = f"{folder}/README.md"

        presentation = get_presentation_file(
            os.path.join(BASE_DIR, folder)
        )

        if presentation:
            extension = os.path.splitext(presentation)[1]
            presentation_link = f"{folder}/Presentation{extension}"
        else:
            presentation_link = ""

        member_text = ", ".join(members)

        readme_cell = (
            f"[README]({readme_link})"
            if os.path.exists(
                os.path.join(BASE_DIR, readme_link.replace("/", os.sep))
            )
            else "Not available"
        )

        if presentation_link:
            presentation_cell = (
                f"[Presentation]({presentation_link})"
            )
        else:
            presentation_cell = "Not available"

        github_cell = (
            f"[GitHub]({github})"
            if github
            else "Not provided"
        )

        rows.append(
            f"| Group {number:02d} | {member_text} | {topic} | "
            f"{readme_cell} | {presentation_cell} | {github_cell} |"
        )

    new_section = (
        "## Project Groups\n\n"
        "| Group | Members | Project Topic | README | Presentation | GitHub |\n"
        "|---|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n\n"
    )

    new_content = (
        content[:start]
        + new_section
        + content[end:]
    )

    try:
        with open(MASTER_README, "w", encoding="utf-8") as f:
            f.write(new_content)

        print("\n✅ Master README regenerated successfully.")

    except Exception as e:
        print(f"\n❌ Failed to update master README:\n{e}")


# ============================================================
# REVIEW CHANGES
# ============================================================

def review_changes():
    print("\n" + "=" * 70)
    print("GIT CHANGES")
    print("=" * 70)

    status = run_git(["git", "status", "--short"])

    if status.returncode != 0:
        print("\n❌ Git status failed.")
        print(status.stderr)
        return

    if not status.stdout.strip():
        print("\n✅ Working tree is clean.")
        return

    print("\nCurrent changes:")
    print("-" * 70)
    print(status.stdout)

    print("\nChange summary:")
    print("-" * 70)

    diff_names = run_git(
        ["git", "diff", "--name-status"]
    )

    if diff_names.stdout.strip():
        print(diff_names.stdout)

    print("\nStatistics:")
    print("-" * 70)

    diff_stat = run_git(
        ["git", "diff", "--stat"]
    )

    if diff_stat.stdout.strip():
        print(diff_stat.stdout)

    press_enter()


# ============================================================
# COMMIT & PUSH
# ============================================================

def commit_and_push():
    print("\n" + "=" * 70)
    print("COMMIT & PUSH")
    print("=" * 70)

    # --------------------------------------------------------
    # 1. Check current status
    # --------------------------------------------------------

    status = run_git(["git", "status", "--short"])

    if status.returncode != 0:
        print("\n❌ Could not read Git status.")
        print(status.stderr)
        return

    if not status.stdout.strip():
        print("\n✅ No changes to commit.")
        return

    print("\nCurrent changes:")
    print("-" * 70)
    print(status.stdout)

    # --------------------------------------------------------
    # 2. SAFE CHANGE SUMMARY
    #
    # IMPORTANT:
    # Do NOT use `git diff` directly.
    #
    # PDFs/PPT/PPTX are binary files and Windows can throw
    # UnicodeDecodeError when Python tries to read their
    # contents as text.
    # --------------------------------------------------------

    print("\nChange summary:")
    print("-" * 70)

    diff_names = run_git(
        ["git", "diff", "--name-status"]
    )

    if diff_names.stdout.strip():
        print(diff_names.stdout)

    diff_stat = run_git(
        ["git", "diff", "--stat"]
    )

    if diff_stat.stdout.strip():
        print("-" * 70)
        print(diff_stat.stdout)

    # --------------------------------------------------------
    # 3. First confirmation
    # --------------------------------------------------------

    print("\n⚠️ Review the changes above carefully.")

    review = input(
        "Have you reviewed these changes? (y/n): "
    ).strip().lower()

    if review != "y":
        print("\n❌ Commit cancelled.")
        return

    # --------------------------------------------------------
    # 4. Strong confirmation
    # --------------------------------------------------------

    print("\n⚠️ WARNING")
    print("The next step will stage ALL current changes.")
    print("This includes:")
    print("  • Modified files")
    print("  • New files")
    print("  • Deleted files")
    print("  • Binary files such as PDF/PPT/PPTX")

    push_confirm = input(
        "\nType PUSH to continue: "
    ).strip()

    if push_confirm != "PUSH":
        print("\n❌ Commit cancelled.")
        return

    # --------------------------------------------------------
    # 5. Stage everything
    # --------------------------------------------------------

    print("\n📦 Staging changes...")

    add_result = run_git(["git", "add", "."])

    if add_result.returncode != 0:
        print("\n❌ Failed to stage changes.")
        print(add_result.stderr)
        return

    print("✅ Changes staged.")

    # --------------------------------------------------------
    # 6. Show EXACT staged changes
    # --------------------------------------------------------

    print("\nStaged changes:")
    print("-" * 70)

    staged = run_git(
        ["git", "diff", "--cached", "--name-status"]
    )

    if staged.returncode != 0:
        print("\n❌ Could not inspect staged changes.")
        print(staged.stderr)
        return

    if not staged.stdout.strip():
        print("\n❌ Nothing was staged.")
        return

    print(staged.stdout)

    # --------------------------------------------------------
    # 7. Show staged statistics
    # --------------------------------------------------------

    staged_stat = run_git(
        ["git", "diff", "--cached", "--stat"]
    )

    if staged_stat.stdout.strip():
        print("-" * 70)
        print(staged_stat.stdout)

    # --------------------------------------------------------
    # 8. FINAL CONFIRMATION
    # --------------------------------------------------------

    print("\n⚠️ FINAL CHECK")
    print("These are the exact files Git is about to commit.")

    final_confirm = input(
        "\nCommit EXACTLY these staged changes? (y/n): "
    ).strip().lower()

    if final_confirm != "y":
        print("\n❌ Commit cancelled.")
        print("The files remain staged.")
        print("Nothing was committed or pushed.")
        return

    # --------------------------------------------------------
    # 9. COMMIT
    # --------------------------------------------------------

    print("\n💾 Creating commit...")

    commit_result = run_git(
        ["git", "commit", "-m", "Update project submissions"]
    )

    if commit_result.stdout.strip():
        print(commit_result.stdout)

    if commit_result.returncode != 0:
        print("\n❌ Commit failed.")
        print(commit_result.stderr)
        return

    print("✅ Commit created.")

    # --------------------------------------------------------
    # 10. PUSH
    # --------------------------------------------------------

    print("\n🚀 Pushing to GitHub...")

    push_result = run_git(
        ["git", "push", "origin", "main"]
    )

    if push_result.stdout.strip():
        print(push_result.stdout)

    if push_result.returncode != 0:
        print("\n❌ Push failed.")
        print(push_result.stderr)
        return

    print("\n" + "=" * 70)
    print("✅ COMMIT AND PUSH SUCCESSFUL")
    print("=" * 70)

    # --------------------------------------------------------
    # 11. Final status
    # --------------------------------------------------------

    final_status = run_git(
        ["git", "status", "--short"]
    )

    if final_status.stdout.strip():
        print("\n⚠️ There are still local changes:")
        print(final_status.stdout)
    else:
        print("\n✅ Working tree is clean.")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        groups = load_groups()

        print("\n")
        print("=" * 70)
        print("        JAVA PROJECT GROUP MANAGER")
        print("=" * 70)

        print("\n1. View Group")
        print("2. Update Project GitHub Link")
        print("3. Add New Group")
        print("4. Update Group README")
        print("5. Update Group Presentation")
        print("6. Delete Group")
        print("7. Regenerate Master README")
        print("8. Review Uncommitted Changes")
        print("9. Commit & Push Changes")
        print("10. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_group(groups)

        elif choice == "2":
            update_github(groups)

        elif choice == "3":
            add_group(groups)

        elif choice == "4":
            update_readme(groups)

        elif choice == "5":
            update_presentation(groups)

        elif choice == "6":
            delete_group(groups)

        elif choice == "7":
            generate_master_readme(groups)

        elif choice == "8":
            review_changes()

        elif choice == "9":
            commit_and_push()

        elif choice == "10":
            print("\nGoodbye 👋")
            break

        else:
            print("\n❌ Invalid option.")
            press_enter()


if __name__ == "__main__":
    main()