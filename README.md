# CommentFold
A Sublime Text plugin to give an overview of your file's structure by folding all other code but comments.

![Comment Fold Preview](comment_fold-preview.gif)

# Default key binding
Use "ctrl+alt+/" to fold all other code and see your comments only for an overview of you file's structure.
Use "shift+ctrl+alt+/" to unfold all your code and get back to the normal view.

Feel free to override these in Sublime Text -> Preferences -> Key Bindings by adding the following lines and change as preferred:

```
{
    "keys": ["ctrl+alt+/"],
    "command": "comment_fold"
	},
{
    "keys": ["shift+ctrl+alt+/"],
    "command": "comment_unfold"
	}
```
