#!/bin/bash

#############################################################################
# Filename : updatesheet
# ============================================================================
#  Object: Integration tool
# ============================================================================
#   Date          Author            Modification
#  2017-04-08	   jw.hu	      Creation
# ============================================================================
#
##############################################################################

SOURCE_SERVER="gerritroot@192.168.31.242"

branchname=${1}
apkversion=${2}
signmode=${3}
modulename=${4}
vercode=${5}
versionnamefinal=${6}
packagenameread=${7}
activityread=${8}
serviceread=${9}
shareduserid=${10}
branchinfo=${11}

echo "branchinfo:${branchinfo}"
echo "shareduserid:${shareduserid}"

swodomain='integration'
info_folder='standaloneapp_info'
updatesheet_trundir=`pwd`
releasedate=`date "+%Y-%m-%d %H:%M:%S"`
info_filename='swo_release.csv'
info_apklist_file='activity_service.csv'
filterbranch="InCallUI,PhoneCommon,ContactsCommon"


echo "****** updatesheet_trundir:${updatesheet_trundir}"

if [ -d ${updatesheet_trundir}/tmpfolder/acuteagappinfo ]; then
   rm -rf  ${updatesheet_trundir}/tmpfolder/acuteagappinfo
fi

mkdir -p ${updatesheet_trundir}/tmpfolder/acuteagappinfo

cd ${updatesheet_trundir}/tmpfolder/acuteagappinfo

git clone $SOURCE_SERVER:\/$swodomain\/${info_folder}

cd ${updatesheet_trundir}

if [ -f ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename} ]; then
  
    if (echo "${filterbranch}" | grep -wq $(echo ${branchname} | cut -d"_" -f1 )); then
        sed -i "/${branchname},${apkversion},${modulename},${signmode}/d" ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}
        echo "${branchname},${apkversion},${modulename},${signmode},${releasedate},${vercode},${versionnamefinal} \
        " >> ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}
    else
        sed -i "/${branchname},${apkversion},${modulename},${signmode}/d" ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}
        echo "${branchname},${apkversion},${modulename},${signmode},${releasedate},${vercode},${versionnamefinal} \
        " >> ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}
    fi

else
    echo "BranchName,ApkVersion,GitName,ReleaseDate,VersionCode,VersionName,BranchInfo" > ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}
    echo "${branchname},${apkversion},${modulename},${signmode},${releasedate},${vercode},${versionnamefinal} \
    " >> ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_filename}

fi

if ( ! (echo "${filterbranch}" | grep -wq $(echo ${branchname} | cut -d"_" -f1 )) ); then

    if [ -f ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_apklist_file} ]; then
        sed -i "/${branchname},${versionnamefinal}/d" ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_apklist_file}
        echo "${branchname},${versionnamefinal},${packagenameread},${shareduserid},${activityread},${serviceread}" >> ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_apklist_file}
    else
        echo "BranchName,VersionName,PackageName,SharedUserId,Activity,Service" > ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_apklist_file}
        echo "${branchname},${versionnamefinal},${packagenameread},${shareduserid},${activityread},${serviceread}" >> ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}/${info_apklist_file}
    fi

fi


cd ${updatesheet_trundir}/tmpfolder/acuteagappinfo/${info_folder}
if ( ! (git status | grep "nothing to commit") );then
    echo "*******************Updating release record***************************"
    git add .
    git commit -am "Jenkins Auto Update For ${branchname} ${apkversion} Internal Release"
    git pull
    git push $SOURCE_SERVER:\/$swodomain\/${info_folder} master
fi
cd ${updatesheet_trundir}

