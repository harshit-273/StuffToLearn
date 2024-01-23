# DataTypes

- There are specific blocks in which some particular data can be stored.

## To store the data of text or string type

### `CHAR(n)`

- If we know the exact size of the text to be entered that we can use with this type.
- We can specify the length of the text with the `n` in braces.
- Trailing spaces are applied if the data to be stored has size smaller than `n`.

### `VARCHAR2(n)`

- If we want to store something with variable length of the text than this would be a good choice.
- It's storage size would be:
```
size of actual no. of characters + fixed size to store the length
```
- Trailing spaces are not applied if the length of the characters is smaller than the `n`

## To store numerical data

- `SMALLINT`, `INTEGER` and `INT` can be used to store the whole numbers.

### `NUMBER(p, s)`

- This data type can be used to store the data with decimal values(also the non-decimal values can be stored).
- `p` represents precision meaning total no. of digits present in the number(including digits before `.` and after it).
- `s` represents scale meaning the no. of digits after `.`.
- If there would be more than `(p-s)` numbers before the `.`, the error would be thrown.

## Miscellaneous

### `DATE`

- It is used to specify the date.
- Format should be:
```
DD-MON-YY
```

### `TIMESTAMP`

- It is used to store date data with precision upto 9 digits of a second. 
- Mostly used for the storing the exact time when the transaction occurred.

### `CLOB`

- For storing the large charater based data which cannot be stored in others due to their size limit.

### `BLOB`

- Storing large binary data like movies, images with size upto 4 GB.