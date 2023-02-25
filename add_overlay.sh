echo "Processing video $1"
width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of json $1 | jq -r '.streams[0].width')
height=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of json $1 | jq -r '.streams[0].height')
echo "Height: $height pixels"
echo "Width: $width pixels"
echo
echo "Resizing overlay..."
convert -resize "${width}x${height}" overlay.png "overlay-${width}x${height}.png"
echo "Done"
echo
echo "Adding overlay to video..."
ffmpeg -y -i $1 -i "overlay-${width}x${height}.png" -filter_complex '[0]overlay=x=0:y=0[out]' -map '[out]' -map '0:a?' "$1-overlay.mp4" &> /dev/null
echo "Done"
