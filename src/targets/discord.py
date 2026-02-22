from lbhelper import CustomDeb, download_file

discord_download_url = "https://discord.com/api/download?platform=linux"

discord_deb = CustomDeb(
    get_deb=lambda : download_file(discord_download_url),
)

targets = [
    discord_deb
]