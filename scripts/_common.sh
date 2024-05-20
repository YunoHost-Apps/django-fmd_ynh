#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

#=================================================
# PERSONAL HELPERS
#=================================================

_install_fmd_venv() {
    ynh_exec_as "$app" python3 -m venv --upgrade "$install_dir/venv"

    venvpython="$install_dir/venv/bin/python3"

    ynh_add_config --template="requirements.txt" --destination="$install_dir/requirements.txt"

    ynh_exec_as "$app" "$venvpython" -m ensurepip
    ynh_exec_as "$app" "$venvpython" -m pip install --upgrade wheel pip setuptools
    ynh_exec_as "$app" "$venvpython" -m pip install --no-deps -r "$install_dir/requirements.txt"
}

#=================================================
# EXPERIMENTAL HELPERS
#=================================================

#=================================================
# FUTURE OFFICIAL HELPERS
#=================================================
