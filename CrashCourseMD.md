```
Headings

-> use number of # on left side of the heading text
-> 1-6 are present

# Heading 1
## Heading 2
### Heading 3
```
# Heading 1
## Heading 2
### Heading 3



```
Italics

-> use * on both the sides
-> use _ on both the sides

*Italics*
_Also Itlalics_
```
*Italics*

_Also Itlalics_


```
Bold

-> use ** on both sides
-> use __ on both sides

**Bold**
__Also Bold__
```
**Bold**

__Also Bold__



```
Strike through

-> use ~~ on both sides

~~StrikeThrough~~
```
~~StrikeThrough~~



```
Horizontal Rule

-> use ---
-> use ___

---
___
 ```
---
___



```
Escape Sequence

-> use \

\*some text\*
```
\*some text\*



```
Blockquotes

-> use >
> Block quotes
```
> Block quotes



```
Links

[Visible Title](linkToPage "TitleVisibleWhenHovered")
-> TitleVisibleWhenHovered is to be used after giving a space to link and in double quotes("...")
-> TitleVisibleWhenHovered is not mandatory
-> linkToPage can be a link in the same page using headings or other page

[google](google.com "google.com") | [other heading](#heading-1 "Top")
```
[google](https://www.google.com "google.com") | [other heading](#heading-1 "Top")
 


```
Unordered Lists

-> use *
-> for nested item use tab and then use *

* item one
* item two
* item three
	* item four
	* item five
```
* item one
* item two
* item three
	* item four
	* item five



```
Ordered Lists

-> use 1.

1. item one
2. item two
3. item three
	 1. item four
	 2. item five
```
1. item one
2. item two
3. item three
	 1. item four
	 2. item five



```
Inline Code Block

-> use ` on both sides

` fmt.Printf("Hello, World!") `
```
` fmt.Printf("Hello, World!") `



```
Image

![ImageName](Imagelink)

![Notes](https://picsum.photos/200/300)
```
![Notes](https://picsum.photos/200/300)



```
Code Blocks

-> use ``` on both the sides
-> LanguageName is not mandatory, but you can use it to specify it for better readability. It is to be used after first triple quotes.

In below I am using ' instead of ` so that it is visible to you.
'''
cout << "Hello, World";
'''

'''python
def function_name(firstParameter, secondParameter):
	""" something with the parameters """
	return output1, output2
'''
```
```cpp
cout << "Hello, World";
```

```python
def function_name(firstParameter, secondParameter):
	""" something with the parameters """
	return output1, output2
```



```
Tables

| Column heading | Column Heading |
| -------------- | -------------- |
| row data       | row data       |
| row data       | row data       |
```
| Column heading | Column Heading |
|----------------|----------------|
| row data       | row data       |
| row data       | row data       |
