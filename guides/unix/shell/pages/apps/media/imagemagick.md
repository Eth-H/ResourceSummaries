# magic
- install
    sudo apt install imagiemagick
- How much to compress by
    
    convert sample.png -quality: [percentageQuality] sample.png
- Change dimensaions of the image, use [WidthxHeight]! to force exact size and ignore aspect ratio

    convert sample.png -resize [WidthxHeight] sample.png

- apply characoal effect
    
    convert sample.png -charcoal 2 sample.png
- rotate

    convert sample.png -rotate 90 sample.png
- batch process images
    
    for file in *.png; do convert $file -rotate 90 rotated-$file; done
