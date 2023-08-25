#!/bin/bash
echo " "
echo -e "\e[1;34m Please enter a commit message: \e[0m"
echo " "
git status

git add .

dt=$(date +'%Y-%m-%d : %H-%M')

git commit -m "Changes perfomed on $dt"

git push

echo " "
echo -e "\e[1;31m Commit perfomed on $dt! \e[0m"
echo " "