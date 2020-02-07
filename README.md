# cmpe273-lab1

## External Sort

* Implemented quck sort on each of the unsorted individual file and stored the sorted result in individual files
* Merged the result of each individual sorted file using min heap to a single file

## Time for External sort

```sh
real    0m0.057s
user    0m0.028s
sys     0m0.013s
```
## Asyncio External Sort

* Converted sort, merge and writing to individual files into async and rest implemented as above

## Time for Asyncio External sort

```sh
real    0m0.094s
user    0m0.023s
sys     0m0.016s
```
