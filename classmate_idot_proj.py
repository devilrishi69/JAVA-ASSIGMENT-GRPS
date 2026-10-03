import json
import shutil
import subprocess
from pathlib import Path

# ==================================================
# REPOSITORY CONFIGURATION
# ==================================================

REPO_DIR = Path(__file__).resolve().parent
GROUPS_DIR = REPO_DIR / "Groups"
DATA_FILE = REPO_DIR / "groups.json"
MASTER_README = REPO_DIR / "README.md"


# ==================================================
# INITIAL GROUP DATA
# ==================================================

INITIAL_GROUPS = {
    "1": {
        "topic": "Scrape Bot",
        "members": ["Rishi", "Balraj", "Pratima", "Naina"],
        "github": ""
    },

    "2": {
        "topic": "Handmade E-Commerce Business",
        "members": [
            "Seha Parasher",
            "Diksha Chaubey",
            "Puja Singh",
            "Kunal Rathore"
        ],
        "github": ""
    },

    "3": {
        "topic": "Affiliate Marketing",
        "members": [
            "Yash Gohar",
            "Devashish Sharma",
            "Tanistha",
            "Ritesh"
        ],
        "github": ""
    },

    "4": {
        "topic": "Article Writing",
        "members": [
            "Ankit Chaudhary",
            "Keshari Nandan Mallik",
            "Sachin Kumar",
            "Dhananjay Thakur",
            "Y. Vijay Chandan"
        ],
        "github": ""
    },

    "5": {
        "topic": "Animation Through Freelancing in Java",
        "members": [
            "Tanu Rathore",
            "Arth Sharma",
            "Ansuman Mistry",
            "Tuleshwar Kumar Yadav"
        ],
        "github": ""
    },

    "6": {
        "topic": "Cloud Kitchen",
        "members": [
            "Aanya",
            "Sandhya"
        ],
        "github": ""
    },

    "7": {
        "topic": "Rural Supply Chain Digitization",
        "members": [
            "Ayush Kumar",
            "Vasudev Choudhary",
            "Saumil Kurre",
            "Shivam Sharma"
        ],
        "github": "https://github.com/Vasudeveloperr/java-project-rural-connect"
    },

    "8": {
        "topic": "Dropshipping Business",
        "members": [
            "Anshuka",
            "Ayush Rajput",
            "Harshwardhan Dhusia",
            "Anjali"
        ],
        "github": ""
    },

    "9": {
        "topic": "Digital Content Creation",
        "members": [
            "Yog Raisagar",
            "Shivam Dewangan",
            "Mahendra Sahu",
            "Nikita Sahu"
        ],
        "github": ""
    },

    "10": {
        "topic": "Rental Platform",
        "members": [
            "Sahil Markam",
            "Devesh Sahu",
            "M. Zaid"
        ],
        "github": ""
    },

    "11": {
        "topic": "Online Yoga and Zumba Course",
        "members": [
            "Pratham Singh",
            "Chirag Gupta",
            "Abhishek Sahu"
        ],
        "github": ""
    },

    "12": {
        "topic": "Amazon KDP",
        "members": [
            "Saurabh Yadav",
            "Shashank Singh",
            "Ankit Kumar",
            "Ayush Khuntiya",
            "Ashutosh Kumar Anand"
        ],
        "github": ""
    }
}


# ==================================================
# DATA FUNCTIONS
# ==================================================

def load_groups():

    if not DATA_FILE.exists():

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                INITIAL_GROUPS,
                file,
                indent=4,
                ensure_ascii=False
            )

        return INITIAL_GROUPS

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_groups(groups):

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            groups,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==================================================
# DISPLAY GROUPS
# ==================================================

def show_groups(groups):

    print("\n" + "=" * 60)
    print("AVAILABLE GROUPS")
    print("=" * 60)

    for number, group in sorted(
        groups.items(),
        key=lambda x: int(x[0])
    ):

        print(
            f"{int(number):02d} - "
            f"{group['topic']}"
        )

    print("=" * 60)


# ==================================================
# CHOOSE GROUP
# ==================================================

def choose_group(groups):

    show_groups(groups)

    number = input(
        "Enter group number: "
    ).strip()

    if number not in groups:

        print("\n❌ Invalid group number.")
        return None

    return number


# ==================================================
# VIEW GROUP
# ==================================================

def view_group(groups):

    number = choose_group(groups)

    if not number:
        return

    group = groups[number]

    print("\n" + "=" * 60)
    print(f"GROUP {int(number):02d}")
    print("=" * 60)

    print(f"Topic: {group['topic']}")

    print("\nMembers:")

    for member in group["members"]:
        print(f"  • {member}")

    print("\nProject GitHub:")

    if group["github"]:
        print(group["github"])
    else:
        print("—")

    print("=" * 60)


# ==================================================
# UPDATE GITHUB LINK
# ==================================================

def update_github(groups):

    number = choose_group(groups)

    if not number:
        return

    group = groups[number]

    print("\nCurrent GitHub link:")

    if group["github"]:
        print(group["github"])
    else:
        print("—")

    new_link = input(
        "\nEnter new GitHub link "
        "(press ENTER to remove): "
    ).strip()

    group["github"] = new_link

    save_groups(groups)

    print("\n✓ GitHub link updated.")


# ==================================================
# ADD NEW GROUP
# ==================================================

def add_group(groups):

    existing_numbers = [
        int(number)
        for number in groups.keys()
    ]

    next_number = max(
        existing_numbers,
        default=0
    ) + 1

    print(
        f"\nNext available group number: "
        f"{next_number}"
    )

    topic = input(
        "Enter project topic: "
    ).strip()

    members = []

    print("\nEnter member names.")
    print(
        "Press ENTER without typing a name "
        "when you are finished."
    )

    while True:

        name = input(
            "Member: "
        ).strip()

        if not name:
            break

        members.append(name)

    github = input(
        "\nProject GitHub URL "
        "(leave blank if none): "
    ).strip()

    groups[str(next_number)] = {
        "topic": topic,
        "members": members,
        "github": github
    }

    save_groups(groups)

    group_folder = (
        GROUPS_DIR /
        f"Group-{next_number:02d}"
    )

    group_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"\n✓ Group {next_number:02d} created."
    )


# ==================================================
# UPDATE GROUP README
# ==================================================

def update_readme(groups):

    number = choose_group(groups)

    if not number:
        return

    group_folder = (
        GROUPS_DIR /
        f"Group-{int(number):02d}"
    )

    readme_file = (
        group_folder /
        "README.md"
    )

    print("\nCurrent README:")
    print(readme_file)

    new_file = input(
        "\nEnter path to the new README file: "
    ).strip().strip('"')

    new_file = Path(new_file)

    if not new_file.exists():

        print("\n❌ File not found.")
        return

    if not new_file.is_file():

        print("\n❌ The path is not a file.")
        return

    if readme_file.exists():

        print(
            "\n⚠️ This will replace "
            "the existing README."
        )

        confirm = input(
            "Continue? (y/n): "
        ).strip().lower()

        if confirm != "y":

            print("\n❌ Update cancelled.")
            return

    group_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(
        new_file,
        readme_file
    )

    print(
        f"\n✓ Group {int(number):02d} "
        f"README updated."
    )


# ==================================================
# FIND PRESENTATION
# ==================================================

def find_presentations(group_number):

    group_folder = (
        GROUPS_DIR /
        f"Group-{int(group_number):02d}"
    )

    if not group_folder.exists():

        return []

    extensions = [
        ".pdf",
        ".pptx",
        ".ppt"
    ]

    return [
        file
        for file in group_folder.iterdir()
        if (
            file.is_file()
            and file.suffix.lower()
            in extensions
        )
    ]


# ==================================================
# UPDATE GROUP PRESENTATION
# ==================================================

def update_presentation(groups):

    number = choose_group(groups)

    if not number:
        return

    group_folder = (
        GROUPS_DIR /
        f"Group-{int(number):02d}"
    )

    group_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    existing_presentations = (
        find_presentations(number)
    )

    if existing_presentations:

        print("\nExisting presentation(s):")

        for file in existing_presentations:

            print(
                f"  • {file.name}"
            )

    else:

        print(
            "\nNo existing presentation found."
        )

    new_file = input(
        "\nEnter path to the new presentation: "
    ).strip().strip('"')

    new_file = Path(new_file)

    if not new_file.exists():

        print("\n❌ File not found.")
        return

    if not new_file.is_file():

        print("\n❌ The path is not a file.")
        return

    allowed_extensions = [
        ".pdf",
        ".pptx",
        ".ppt"
    ]

    if new_file.suffix.lower() not in allowed_extensions:

        print(
            "\n❌ Unsupported presentation format."
        )

        print(
            "Allowed: .pdf, .pptx, .ppt"
        )

        return

    confirm = input(
        "\nReplace the current presentation? (y/n): "
    ).strip().lower()

    if confirm != "y":

        print("\n❌ Update cancelled.")
        return

    # Remove old presentations
    for old_file in existing_presentations:

        old_file.unlink()

    # Keep the new file's filename
    destination = (
        group_folder /
        new_file.name
    )

    shutil.copy2(
        new_file,
        destination
    )

    print(
        f"\n✓ Group {int(number):02d} "
        f"presentation updated."
    )

    print(
        f"Saved as: {destination.name}"
    )


# ==================================================
# FIND PRESENTATION FOR README
# ==================================================

def find_presentation(group_number):

    presentations = (
        find_presentations(group_number)
    )

    if not presentations:

        return None

    return presentations[0]


# ==================================================
# GENERATE MASTER README
# ==================================================

def generate_master_readme(groups):

    if not MASTER_README.exists():

        print(
            "\n❌ Master README.md not found."
        )

        return

    with open(
        MASTER_README,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    start_marker = "## Project Groups"
    end_marker = "## Folder Structure"

    start_index = content.find(
        start_marker
    )

    end_index = content.find(
        end_marker
    )

    if start_index == -1:

        print(
            "\n❌ Could not find "
            "'## Project Groups'."
        )

        print(
            "README was NOT changed."
        )

        return

    if end_index == -1:

        print(
            "\n❌ Could not find "
            "'## Folder Structure'."
        )

        print(
            "README was NOT changed."
        )

        return

    table = []

    table.append(
        "## Project Groups\n"
    )

    table.append(
        "| Group | Members | Project Topic | README | Presentation | Project GitHub |"
    )

    table.append(
        "|---|---|---|---|---|---|"
    )

    for number, group in sorted(
        groups.items(),
        key=lambda x: int(x[0])
    ):

        group_number = int(number)

        group_folder = (
            f"Groups/Group-{group_number:02d}"
        )

        readme_file = (
            GROUPS_DIR /
            f"Group-{group_number:02d}" /
            "README.md"
        )

        presentation = (
            find_presentation(
                group_number
            )
        )

        # README
        if readme_file.exists():

            readme_link = (
                f"[README]"
                f"({group_folder}/README.md)"
            )

        else:

            readme_link = "—"

        # Presentation
        if presentation:

            presentation_link = (
                f"[Presentation]"
                f"({group_folder}/{presentation.name})"
            )

        else:

            presentation_link = "—"

        # GitHub
        if group["github"]:

            github_link = (
                f"[GitHub]"
                f"({group['github']})"
            )

        else:

            github_link = "—"

        members = ", ".join(
            group["members"]
        )

        table.append(
            f"| Group {group_number:02d} | "
            f"{members} | "
            f"{group['topic']} | "
            f"{readme_link} | "
            f"{presentation_link} | "
            f"{github_link} |"
        )

    table.append("")

    new_section = "\n".join(table)

    new_content = (
        content[:start_index]
        + new_section
        + content[end_index:]
    )

    confirm = input(
        "\nRegenerate the Project Groups table? (y/n): "
    ).strip().lower()

    if confirm != "y":

        print(
            "\n❌ README generation cancelled."
        )

        return

    with open(
        MASTER_README,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(new_content)

    print(
        "\n✓ Master README updated."
    )


# ==================================================
# COMMIT & PUSH
# ==================================================

def commit_and_push():

    print("\n" + "=" * 60)
    print("GIT STATUS")
    print("=" * 60)

    status = subprocess.run(
        [
            "git",
            "status",
            "--short"
        ],
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )

    if status.returncode != 0:

        print(
            "\n❌ Could not read Git status."
        )

        print(status.stderr)

        return

    if not status.stdout.strip():

        print(
            "\n✓ No changes to commit."
        )

        return

    print(status.stdout)

    confirm = input(
        "\nCommit and push these changes? (y/n): "
    ).strip().lower()

    if confirm != "y":

        print(
            "\n❌ Commit cancelled."
        )

        return

    # ------------------------------
    # GIT ADD
    # ------------------------------

    add = subprocess.run(
        [
            "git",
            "add",
            "."
        ],
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )

    if add.returncode != 0:

        print(
            "\n❌ Git add failed."
        )

        print(add.stderr)

        return

    # ------------------------------
    # GIT COMMIT
    # ------------------------------

    commit = subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "Update project submissions"
        ],
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )

    if commit.returncode != 0:

        print(
            "\n❌ Git commit failed."
        )

        print(commit.stderr)

        return

    print(
        "\n✓ Changes committed."
    )

    # ------------------------------
    # GIT PUSH
    # ------------------------------

    push = subprocess.run(
        [
            "git",
            "push",
            "origin",
            "main"
        ],
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )

    if push.returncode != 0:

        print(
            "\n❌ Git push failed."
        )

        print(push.stderr)

        return

    print(
        "\n✓ Changes pushed to GitHub successfully!"
    )


# ==================================================
# MAIN MENU
# ==================================================

def main():

    groups = load_groups()

    while True:

        print("\n")
        print("=" * 60)
        print(
            "       PROJECT REPOSITORY MANAGER"
        )
        print("=" * 60)

        print(
            "1. View Group"
        )

        print(
            "2. Update Project GitHub Link"
        )

        print(
            "3. Add New Group"
        )

        print(
            "4. Update Group README"
        )

        print(
            "5. Update Group Presentation"
        )

        print(
            "6. Regenerate Master README"
        )

        print(
            "7. Commit & Push Changes"
        )

        print(
            "8. Exit"
        )

        print("=" * 60)

        choice = input(
            "Choose an option: "
        ).strip()

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

            generate_master_readme(groups)

        elif choice == "7":

            commit_and_push()

        elif choice == "8":

            print(
                "\nGoodbye!"
            )

            break

        else:

            print(
                "\n❌ Invalid choice."
            )


# ==================================================
# START PROGRAM
# ==================================================

if __name__ == "__main__":
    main()