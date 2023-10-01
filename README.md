# abell
Simple stego tool for educational purposes

### dependences
Install PIL and filetype

`pip install pillow`<br>
`pip install filetype`

### usage
Default commands

hide message in image:<br>
`python3 abell.py --hide [image file] [message]`<br>
show hidden message in image:<br>
`python3 abell.py --show [image file]`

### notes
- The tool works well with short messages (max 15-20 characters)<br>
- For messages with spaces use quotation marks `python3 abell.py --hide image.png "hello world"`<br>
- The output file is a png image<br>
