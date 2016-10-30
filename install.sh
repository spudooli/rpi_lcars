#!/bin/bash
# Installation script for LCARS UI

# Group ownership for state files
GROUP="lcars"

# Directory to install state files
INSTALL_DIR="/var/lib/lcars"

checkgroup()
{
  if grep -q $GROUP /etc/group
  then
    echo "Group '$GROUP' exists."
  else
    echo "Group '$GROUP' does not exist, can't set file permissions."
    exit
  fi
}

installdeps()
{
  # Install the required packages
  echo -n "Updating package list..."
  apt-get update > /dev/null
  echo "OK"
  echo "Checking dependencies..."
  apt-get install python python-pygame python-pil
}

createdir()
{
  # First check if group exists
  checkgroup
  # Create /var directories
  echo "Creating $INSTALL_DIR"
  mkdir -p $INSTALL_DIR
  # Set permissions
  echo "Setting owner of $INSTALL_DIR to '$GROUP'"
  chown root:$GROUP $INSTALL_DIR
  chmod g+w $INSTALL_DIR
  chmod g+s $INSTALL_DIR
  chmod 775 $INSTALL_DIR
  echo "OK"
}

checkuser()
{
  # Make sure the user is running with root-level permissions
  if [ $UID -ne 0 ]; then
  	echo "Sorry, you need to have root permissions to run this script."
  	echo "Either login as root, or run this though sudo."
  	exit
  fi
}

# Execution starts here
case $1 in
'uninstall')
  checkuser
  echo "Removing $INSTALL_DIR"
  rm -rf $INSTALL_DIR
;;
'deps')
  checkuser
  installdeps
;;
'wipe')
  rm $INSTALL_DIR/*
;;
'makegroup')
  checkuser
  echo "Creating group '$GROUP'..."
  groupadd $GROUP
;;
'help')
echo "LCARS Installations script"
echo "usage: $0 uninstall|makegroup|wipe|deps"
echo ""
echo "If no argument is given, script will attempt installation."
;;
*)
  checkuser
  installdeps
  createdir
esac
