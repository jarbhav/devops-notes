# `Headers`

```md
# This is a H1 header
## This is a H2 header
### This is a H3 header
#### This is a H4 header
##### This is a H5 header
```
# This is a H1 header
## This is a H2 header
### This is a H3 header
#### This is a H4 header
##### This is a H5 header


# `Blockquotes`

```md
> Single line quote
>> Nested quote
>> multiple line
>> quote
```
> Single line quote
>> Nested quote
>> multiple line
>> quote

# `Horizontal rules`

To add a horizontal rule, add a line that's a series of dashes *--. The line above the line containing the --- must be blank.

```md
above
 
----
below
```
above

----
below


# `Emphasis (bold, italics, strikethrough)`
|Result|Syntax|
-------|-------
|To apply italics| surround the text with an asterisk * or underscore _|
|To apply bold| surround the text with double asterisks **|
|To apply strikethrough| surround the text with double tilde characters ~~|

```md
Use _emphasis_ in comments to express **strong** opinions and point out ~~corrections~~  
**_Bold, italicized text_**  
**~~Bold, strike-through text~~**
```
Use _emphasis_ in comments to express **strong** opinions and point out ~~corrections~~  
**_Bold, italicized text_**  
**~~Bold, strike-through text~~**

# `Code highlighting`

\```

sudo apt install neofetch 

\```

```
sudo apt install neofetch  
```

# `Tables`

* Place each table row on its own line.
* Separate table cells using the pipe character |.
* The first two lines of a table set the column headers and the alignment of elements in the table.
* Use colons (:) when dividing the header and body of tables to specify column alignment (left, center, right).

```md
| Heading 1 | Heading 2 | Heading 3 |  
|-----------|:-----------:|-----------:|  
| Cell A1 | Cell A2 | Cell A3 |  
| Cell B1 | Cell B2 | Cell B3<br/>second line of text |
```

| Heading 1 | Heading 2 | Heading 3 |  
|-----------|:-----------:|-----------:|  
| Cell A1 | Cell A2 | Cell A3 |  
| Cell B1 | Cell B2 | Cell B3<br/>second line of text |

# `Lists`

## `Ordered or numbered lists`

```md
1. First item.
1. Second item.
1. Third item.
```
1. First item.
1. Second item.
1. Third item.

## `Bulleted lists`

```md
* Item 1
* Item 2
* Item 3
```
* Item 1
* Item 2
* Item 3

## `Nested Lists`

```md
1. First item.
   - Item 1
   - Item 2
   - Item 3
1. Second item.
   - Nested item 1
      - Further nested item 1
      - Further nested item 2
      - Further nested item 3
   - Nested item 2
   - Nested item 3
```

1. First item.
   - Item 1
   - Item 2
   - Item 3
1. Second item.
   - Nested item 1
      - Further nested item 1
      - Further nested item 2
      - Further nested item 3
   - Nested item 2
   - Nested item 3

# `Links`

```md
[Notes Repo](https://github.com/jarbhav/devops-notes)
```

[Notes Repo](https://github.com/jarbhav/devops-notes)

# `Images`

```md
![Instructions](images/md/INSTRUCTIONS.png)
```
![Instructions](images/md/INSTRUCTIONS.png)

# `Task lists`
To create a task list, preface list items with a hyphen and space followed by [ ]. To mark a task as complete, use [x].

```md
- [ ] A  
- [ ] B  
- [ ] C  
- [x] A  
- [x] B  
- [x] C  
```
- [ ] A  
- [ ] B  
- [ ] C  
- [x] A  
- [x] B  
- [x] C  

# `Escaping`
BACKSLASH ESCAPES
Markdown allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown’s formatting syntax. For example, if you wanted to surround a word with literal asterisks you can use backslashes before the asterisks, like this:

```md
\*literal asterisks\*
```

\*literal asterisks\*

# `Mentioning people and teams`
You can mention a person or team on GitHub by typing `@` plus their username or team name. This will trigger a notification and bring their attention to the conversation. People will also receive a notification if you edit a comment to mention their username or team name. For more information about notifications, see "About notifications."

Note: A person will only be notified about a mention if the person has read access to the repository and, if the repository is owned by an organization, the person is a member of the organization.

# `Referencing issues and pull requests`
You can bring up a list of suggested issues and pull requests within the repository by typing` #`. Type the issue or pull request number or title to filter the list, and then press either tab or enter to complete the highlighted result.


# Other resources
Github guidelines for Markdown[^1]

[^1]:https://docs.github.com/en/get-started/writing-on-github