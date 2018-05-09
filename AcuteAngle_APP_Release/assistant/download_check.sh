#!/bin/bash
#############################################################################
# Filename : download_check.sh
# ============================================================================
#  Object: app tool
# ============================================================================
#   Date          Author            Modification
#  2017-04-08	  jw.hu	            Creation
#  Main use:
#  download Project_Release to local folder
##############################################################################

HOST='192.168.31.242'
USER='acuteangleftp'
PASS='sjx1234'

project_sync=$1
releasedir=$2
syncpath=$3
versionsync=$4
apknamesigned=$5
acuteag_release_dir="${6}"

branch_name_release="${7}"

project_remote="/APP_Release"

echo "****** Versionsync:${versionsync}"
echo "****** Remote:${project_remote}/${project_sync}/${releasedir}"

lftp -u ${USER},${PASS} ftp://${HOST} <<EOF
cd ${project_remote}/${project_sync}/${releasedir}
mirror $versionsync $versionsync
bye
EOF

if (!(find $versionsync -name "*.apk" | grep ".apk") ) && (!(find $versionsync -name "*.jar" | grep ".jar") ); then
  echo "*****************************Error*****************************"
  echo "Can't find apk/jar. Please check if apk/jar has been generated."
  echo "***************************************************************"
  exit 1
fi


if  [ "$apknamesigned" != "" ]; then
  if [ ! -f $versionsync/$apknamesigned ]; then
    ApkNameSignedBuild=`ls $versionsync | grep "_signed"`
    echo "*****************************Error*****************************"
    echo "The apk is being released:"
    echo "$apknamesigned"
    echo "Have generated apk name is:"
    echo "$ApkNameSignedBuild"
    echo "Maybe set sign_mode differently."
    echo "***************************************************************"
    exit 1
  else
    echo "****** Apk Name is Correct on 192.168.1.108 FTP Project_Rlease folder."
  fi
else
  echo "******Maybe Thirdparty Apk or Jar Package."
fi

echo "****** Sync acuteag"

if [ ! -d ${acuteag_release_dir}/acuteag-apps/${project_sync} ];then
    echo "****** Error:${acuteag_release_dir}/acuteag-apps/${project_sync} has not been set,Pls contacts Admin!"
    exit 1
fi


out_module_name=`echo ${apknamesigned} | sed "s/.apk//"`
echo "****** Out_module_version:${out_module_name}"

old_module_path=`ls ${acuteag_release_dir}/acuteag-apps/${project_sync}/*.apk`
old_module_name=`basename ${old_module_path}`
echo "****** Old_module_version:${old_module_name}"

echo "****** Cp ${versionsync}/${apknamesigned} ${acuteag_release_dir}/acuteag-apps/${project_sync}/${out_module_name}"

cp ${versionsync}/${apknamesigned} ${acuteag_release_dir}/acuteag-apps/${project_sync}/${out_module_name}.apk


cd ${acuteag_release_dir}

if ( ! ((git status | grep "nothing to commit") || (git status | grep "无文件要提交") ));then
    echo "****** Jenkins Auto Update ${out_module_name}.apk"

    git checkout ${branch_name_release}
    git pull

    git add .
    git rm acuteag-apps/${project_sync}/${old_module_name}
    git commit -am "jenkins auto update ${out_module_name}.apk"

    git push origin HEAD:${branch_name_release}
   
fi

echo "****** Done."
