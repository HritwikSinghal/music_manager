"""Entry point for music_manager."""

# from .cli import main  # pragma: no cover
from minim import itunes, qobuz, spotify, tidal


def test():
    text = """
    vga - (Optional) The VGA configuration.

        memory - (Optional) The VGA memory in megabytes (defaults to 16).
        type - (Optional) The VGA type (defaults to std).
            cirrus - Cirrus (deprecated since QEMU 2.2).
            none - No VGA device.
            qxl - SPICE.
            qxl2 - SPICE Dual Monitor.
            qxl3 - SPICE Triple Monitor.
            qxl4 - SPICE Quad Monitor.
            serial0 - Serial Terminal 0.
            serial1 - Serial Terminal 1.
            serial2 - Serial Terminal 2.
            serial3 - Serial Terminal 3.
            std - Standard VGA.
            virtio - VirtIO-GPU.
            virtio-gl - VirtIO-GPU with 3D acceleration (VirGL). VirGL support needs some extra libraries that aren’t installed by default. See the Proxmox documentation section 10.2.8 for more information.
            vmware - VMware Compatible.
        clipboard - (Optional) Enable VNC clipboard by setting to vnc. See the Proxmox documentation section 10.2.8 for more information.
    """

    my_text = [x for x in text.splitlines() if x.strip()]
    final_code = []
    for line in my_text:
        line_indent = len(line) - len(line.strip())
        # print(line)
        if line_indent == 0:
            description = line.split(")", 1)[1]
        elif line_indent == 4:
            # actual option
            option = line.split("-")[0].strip()
            option_type = "bool" if "true" in line.lower() or "false" in line.lower() else "string"

            if "optional" in line.lower():
                optional = f"optional({option_type})"
            else:
                optional = f"{option_type}"

            comment = line.split(")", 1)[1].strip()
            print(f"{option} = {optional} # {comment}")
        elif line_indent == 8:
            # types of values to accept
            pass

        # print()


# https://developer.tidal.com/dashboard
# cd ~/test/
# git clone https://github.com/bbye98/minim.git
# cd <project dir> && pipenv shell
# pipenv install ~/test/minim

# AS soon as you enter the project folder, you will execute python version specified locally using pyenv.
# EVEN befor entering pipenv shell (because pyenv is not Pipenv, duh!)

# https://old.reddit.com/r/pycharm/comments/j92p0e/pycharm_with_pipenv_integration/

def main():
    client_itunes = itunes.SearchAPI()


if __name__ == "__main__":  # pragma: no cover
    main()
    # test()
