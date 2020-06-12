HASHING is a data structure that is used to store a large number of data,which can be accessed in o(1) time by operations such as INSERT,DELETE and SEARCH.
- Hashing is an improvement over Direct Access Table.
- The idea is to use the hash function that converts any key to a smaller number and uses the small number as index in a table called hash table.And the data is stored at the position of the index value used in Hashtable.
- HashFunction:A function that converts a given number to a small practical integer value. The mapped integer value is used as an index in the hash table.
- In simple terms, a hash function maps a big number or string to a small integer that can be used as an index in the hash table.
 A good hash function should have following properties
- 1) Efficiently computable.
- 2) Should uniformly distribute the keys (Each table position equally likely for each key)
HashTable:An array that stores pointers to records corresponding to a given phone number. An entry in the hash table is NIL if no existing phone number has hash function value equal to the index for the entry.
- CollisionHandling:Since a hash function gets us a small number for a big key, there is a possibility that two keys might result in the same value. The situation where a newly inserted key maps to an already occupied slot in the hash table is called collision and must be handled using some collision handling technique. There are many ways to handle collisions.In this project the collision handling technique used is:
Chaining:The idea is to make each cell of the hash table point to a linked list of records that have the same hash function value. Chaining is simple, but requires additional memory outside the table. 

In order to run this program,the basic requirements that needs to be met are:
- 1)Python3 or higher version 
- 2)Python IDE(recommended:Spyder)
- 3)Dataset on which you need to operate
 In order to run this code,the following steps are required:
- 1)Import the packages such as CSV,Time,Pandas
- 2)Add your input and result file paths to the source_file_path and destination_file_path.
- 3)Run the program and follow the instructions displayed on the console. 
