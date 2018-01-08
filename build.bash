#!/bin/bash

################################
# This script builds a release #
################################

#reasons for creating building release script:

#This script could be put into Jenkins

#I started out thinking .spec file was the starting point. It's not.
#Given up on .spec file generating all the correct info with tricks like:
#%define selinux_policyver %(sed -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp 2> /dev/null)
#%define   _build_number %(echo ${BUILD_NUMBER:-1})

#With .spec method only - You would need to run spectool -g -R SPECS/ply.spec to pull down source
#before running rpmbuild against the .spec file.

#When do you declare version numbers and releases? SCRUM meetings?
#During creation of git repo?

PACKAGE="bcc-eBPF-tools"
VER_MAJOR="3"
RELEASE="1.0"
DESC="\"Version 3 release\""
SPEC="$PACKAGE.spec"
LONG_SUMMARY="\"Release to add fix on post build errors\""
PACKAGER="michael.chanslor@gmail.com"
REAL_NAME="Michael D. Chanslor"
DATE=$(date +"%a %b %e %Y")
FIX="- This is a bug fix for compile errors"
CHANGELOG="* $DATE $REAL_NAME <$PACKAGER> $VER_MAJOR-$RELEASE"


printf -v CHANGEMESSAGE "$CHANGELOG \n$FIX"
echo "$CHANGEMESSAGE" > $SPEC

#CHANGEMESSAGE=$(echo $CHANGELOG)
#echo $CHANGEMESSAGE


exit 0

# RPM WORK:
#----------
# bump spec to add rpm release notes
# Updates Packager: in .spec
# NO MORE: rpmdev-bumpspec -c $LONG_SUMMARY -u $PACKAGER $SPEC
# bumpspec clobbers sed statements

sed -i 's/_VERSION_/'"$VER_MAJOR"'/g' $SPEC
sed -i 's/_RELEASE_/'"$RELEASE"'/g' $SPEC

# GIT WORK:
#----------
# Creates a _VERSION_
git tag -a $PACKAGE-$VER_MAJOR-$RELEASE -m $DESC
git push origin master --tags


#Build by downloading from github:

# Download source based on waht in .spec
# /usr/bin/spectool -g -R SPECS/ply.spec

#
#  

