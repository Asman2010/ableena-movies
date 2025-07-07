import subprocess


def stream(torrent_id: str):
    """Main function to run the streamer logic."""

    command = ["webtorrent"]

    print("\nPreparing to stream...")
    command.extend(["--mpv"])
    action_description = "Streaming"

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


# if __name__ == "__main__":
#     stream(
#         "magnet:?xt=urn:btih:D1AD4F4CCCC44E6227283BD334487E777EB88EDC&dn=American.Psycho.2000.Remastered.1080p.BluRay.X264.AC3.Wi&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.bittor.pw%3A1337%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce"
#     )
