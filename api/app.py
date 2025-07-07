import subprocess
import sys


def main():
    """Main function to run the streamer logic."""
    print("--- Simple WebTorrent Python Streamer ---")

    torrent_id = input("Enter magnet link or info hash (Please use double quotes):\n> ")

    print("\nChoose an action:")
    print("  [1] Stream the video (requires a player like MPV or VLC)")
    print("  [2] Download the files to the current directory")

    choice = input("Enter your choice (1 or 2): ")

    command = ["webtorrent"]

    if choice == "1":
        print("\nPreparing to stream...")
        command.extend(["--mpv"])
        action_description = "Streaming"
    elif choice == "2":
        print("\nPreparing to download...")
        action_description = "Downloading"
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    command.append(torrent_id)

    print(f"Action: {action_description}")
    print(f"Executing command: {' '.join(command)}")
    print("-" * 40)

    try:
        subprocess.run(command, check=True)
        print("-" * 40)
        print(f"{action_description} finished successfully.")
    except FileNotFoundError:
        print("\n[ERROR] 'webtorrent' command not found.")
        print("Please make sure you have installed webtorrent-cli globally:")
        print("  npm install webtorrent-cli -g")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] An error occurred while running webtorrent: {e}")
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting.")


if __name__ == "__main__":
    main()
