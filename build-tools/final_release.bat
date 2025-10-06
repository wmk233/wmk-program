@echo off
title 水印工具最终发布脚本

echo 水印工具最终发布脚本
echo ====================

echo 正在创建发布目录...
if not exist final-release mkdir final-release

echo 正在复制发布文件...
xcopy watermark-tool-v1.0.0-release final-release\watermark-tool-v1.0.0-release\ /E /I /Y

echo 正在创建zip文件...
powershell Compress-Archive -Path watermark-tool-v1.0.0-release -DestinationPath final-release\watermark-tool-v1.0.0.zip -Force

echo 正在复制说明文件...
copy FINAL_RELEASE.md final-release\README.md

echo.
echo ====================
echo 发布完成！
echo 发布文件位于: final-release\
echo ====================

pause