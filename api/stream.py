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
#         "magnet:?xt=urn:btih:c9edf10480be4e857251aee74d518513ae93788e&dn=www.1TamilMV.onl%20-%203BHK%20%282025%29%20Tamil%20HQ%20PreDVD%20-%20x264%20-%20HQ%20Clean%20Aud%20-%20250MB.mkv&xl=289974677&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.vraphim.com%3A6969%2Fannounce&tr=http%3A%2F%2Fbt.okmp3.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Fu4.trakx.crim.ist%3A1337%2Fannounce&tr=udp%3A%2F%2Fbt.ktrackers.com%3A6666%2Fannounce&tr=https%3A%2F%2Ftrackers.mlsub.net%3A443%2Fannounce&tr=udp%3A%2F%2Fttk2.nbaonlineservice.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.fnix.net%3A6969%2Fannounce&tr=udp%3A%2F%2Fevan.im%3A6969%2Fannounce&tr=udp%3A%2F%2Fmartin-gebhardt.eu%3A25%2Fannounce&tr=udp%3A%2F%2Ftracker.deadorbit.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Fbandito.byterunner.io%3A6969%2Fannounce&tr=udp%3A%2F%2Ftrackarr.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftr4ck3r.duckdns.org%3A6969%2Fannounce&tr=http%3A%2F%2Ftaciturn-shadow.spb.ru%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.bjut.jp%3A443%2Fannounce&tr=https%3A%2F%2Fapi.ipv4online.uk%3A443%2Fannounce&tr=udp%3A%2F%2Fismaarino.com%3A1234%2Fannounce&tr=https%3A%2F%2Ftracker.moeking.me%3A443%2Fannounce&tr=http%3A%2F%2Ftracker.renfei.net%3A8080%2Fannounce&tr=https%3A%2F%2Ftr.nyacat.pw%3A443%2Fannounce&tr=http%3A%2F%2Ftracker.bt4g.com%3A2095%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fwepzone.net%3A6969%2Fannounce&tr=udp%3A%2F%2Fp2p.publictracker.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Fr.l5.ca%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.gcrenwp.top%3A443%2Fannounce&tr=https%3A%2F%2Ftr.zukizuki.org%3A443%2Fannounce&tr=udp%3A%2F%2Fudp.tracker.projectk.org%3A23333%2Fannounce&tr=http%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.mywaifu.best%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fodd-hd.fr%3A6969%2Fannounce&tr=udp%3A%2F%2Fbittorrent-tracker.e-n-c-r-y-p-t.net%3A1337%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta.me%3A2710%2Fannounce&tr=https%3A%2F%2Ftracker.yemekyedim.com%3A443%2Fannounce&tr=udp%3A%2F%2Ft.overflow.biz%3A6969%2Fannounce&tr=udp%3A%2F%2Fserpb.vpsburti.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=udp%3A%2F%2Fec2-18-191-163-220.us-east-2.compute.amazonaws.com%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.lilithraws.org%3A443%2Fannounce&tr=http%3A%2F%2Ftr1.aag.moe%3A2095%2Fannounce&tr=https%3A%2F%2Ft.213891.xyz%3A443%2Fannounce&tr=http%3A%2F%2Fipv4.rer.lol%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker.tryhackx.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.filemail.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fd40969.acod.regrucolo.ru%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.breizh.pm%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.srv00.com%3A6969%2Fannounce&tr=http%3A%2F%2Fipv4announce.sktorrent.eu%3A6969%2Fannounce&tr=udp%3A%2F%2Fseedpeer.net%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.yume-hatsuyuki.moe%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fns1.monolithindustries.com%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.aburaya.live%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.leechshield.link%3A443%2Fannounce&tr=udp%3A%2F%2Ftr.movian.eu%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.cloudit.top%3A443%2Fannounce&tr=udp%3A%2F%2Fwww.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.0x7c0.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.darkness.services%3A6969%2Fannounce&tr=udp%3A%2F%2Fmikrotik2.draatman.net%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker-zhuqiy.dgj055.icu%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.dstud.io%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentracker.io%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.gmi.gd%3A6969%2Fannounce&tr=https%3A%2F%2Ftr2.trkb.ru%3A443%2Fannounce&tr=https%3A%2F%2Ftorrent.tracker.durukanbal.com%3A443%2Fannounce&tr=https%3A%2F%2Fretracker.x2k.ru%3A443%2Fannounce&tr=udp%3A%2F%2Ftr3.ysagin.top%3A2715%2Fannounce&tr=udp%3A%2F%2Ftracker.kmzs123.tk%3A17272%2Fannounce&tr=udp%3A%2F%2Fcq.kmzs123.cn%3A17272%2Fannounce)"
#     )
