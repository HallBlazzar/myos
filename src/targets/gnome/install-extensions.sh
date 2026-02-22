#!/bin/bash

set -xe

urls=(
"https://extensions.gnome.org/extension/36/lock-keys/"
"https://extensions.gnome.org/extension/1460/vitals/"
#"https://extensions.gnome.org/extension/3843/just-perfection/"
"https://extensions.gnome.org/extension/755/hibernate-status-button/"
"https://extensions.gnome.org/extension/2/move-clock/"

"https://extensions.gnome.org/extension/307/dash-to-dock/"
"https://extensions.gnome.org/extension/4099/no-overview/"
# latest version could cause fcitx5 config tool missing
#"https://extensions.gnome.org/extension/261/kimpanel/"
#"https://extensions.gnome.org/extension/615/appindicator-support/"
)

EXTENSION_DIR="/etc/skel/.local/share/gnome-shell/extensions"

echo "Create extension directory $EXTENSION_DIR"
mkdir -p $EXTENSION_DIR

# Loop through each URL
for url in "${urls[@]}"; do
  echo "url = ${url}"
  # get package metadata
  id=$(echo "${url}" | cut --delimiter=/ --fields=5)
  url_pkg_metadata="https://extensions.gnome.org/extension-info/?pk=${id}"
  # Extract data for each extension
  install_dir_id=$(curl -s "$url_pkg_metadata" | jq -r '.uuid')
  install_dir="$EXTENSION_DIR/$install_dir_id"
  uuid=$(curl -s "$url_pkg_metadata" | jq -r '.uuid' | tr -d '@')
  latest_extension_version=$(curl -s "$url_pkg_metadata" | jq -r '.shell_version_map | to_entries | max_by(.value.version) | .value.version')
  latest_shell_version=$(curl -s "$url_pkg_metadata" | jq -r '.shell_version_map | to_entries | max_by(.value.version) | .key')

  # get  package
  filename="${uuid}.v${latest_extension_version}.shell-extension.zip"
  url_pkg="https://extensions.gnome.org/extension-data/${filename}"
  wget -P /tmp "${url_pkg}"

  # install package
  unzip /tmp/${filename} -d $install_dir

  if [ -d "$install_dir/schemas"]; then
      echo "Schema directory exists. Compile it."
      # ensure no un-compiled schemas
      glib-compile-schemas "$install_dir/schemas/"
  fi

  # remove source package
  rm -rf /tmp/${filename}

  # Print the results
  echo "For URL: $url"
  echo "UUID: $uuid"
  echo "Latest extension version: $latest_extension_version"
  echo "Latest shell version: $latest_shell_version"
  echo "--------------------------------------"
done

# Making extension globally readable
chmod 755 -R $EXTENSION_DIR
