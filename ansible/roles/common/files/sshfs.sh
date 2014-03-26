#! env /bin/bash
src=echo $SSH_CLIENT | awk '{ print $1}'
sshfs schuppo@$src:"/Users/schuppo/Centos 6.5" /mnt -o uid=500 -o gid=500 -o allow_other
