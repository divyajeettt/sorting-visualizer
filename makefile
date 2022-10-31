all: create, compile, link

create:
	mkdir -p ./bin/dll
	mkdir -p ./bin/o

compile:
	gcc -o ./bin/o/bitonicSort.o -c ./src/c/bitonicSort.c
	gcc -o ./bin/o/bubbleSort.o -c ./src/c/bubbleSort.c
	gcc -o ./bin/o/cocktailShakerSort.o -c ./src/c/cocktailShakerSort.c
	gcc -o ./bin/o/cycleSort.o -c ./src/c/cycleSort.c
	gcc -o ./bin/o/doubleSelectionSort.o -c ./src/c/doubleSelectionSort.c
	gcc -o ./bin/o/heapSort.o -c ./src/c/heapSort.c
	gcc -o ./bin/o/insertionSort.o -c ./src/c/insertionSort.c
	gcc -o ./bin/o/mergeSort.o -c ./src/c/mergeSort.c
	gcc -o ./bin/o/oddEvenSort.o -c ./src/c/oddEvenSort.c
	gcc -o ./bin/o/quickSort.o -c ./src/c/quickSort.c
	gcc -o ./bin/o/reverseSelectionSort.o -c ./src/c/reverseSelectionSort.c
	gcc -o ./bin/o/selectionSort.o -c ./src/c/selectionSort.c
	gcc -o ./bin/o/timSort.o -c ./src/c/timSort.c

link:
	gcc -o ./bin/dll/bitonicSort.dll -s --shared ./bin/o/bitonicSort.o
	gcc -o ./bin/dll/bubbleSort.dll -s --shared ./bin/o/bubbleSort.o
	gcc -o ./bin/dll/cocktailShakerSort.dll -s --shared ./bin/o/cocktailShakerSort.o
	gcc -o ./bin/dll/cycleSort.dll -s --shared ./bin/o/cycleSort.o
	gcc -o ./bin/dll/doubleSelectionSort.dll -s --shared ./bin/o/doubleSelectionSort.o
	gcc -o ./bin/dll/heapSort.dll -s --shared ./bin/o/heapSort.o
	gcc -o ./bin/dll/insertionSort.dll -s --shared ./bin/o/insertionSort.o
	gcc -o ./bin/dll/mergeSort.dll -s --shared ./bin/o/mergeSort.o
	gcc -o ./bin/dll/oddEvenSort.dll -s --shared ./bin/o/oddEvenSort.o
	gcc -o ./bin/dll/quickSort.dll -s --shared ./bin/o/quickSort.o
	gcc -o ./bin/dll/reverseSelectionSort.dll -s --shared ./bin/o/reverseSelectionSort.o
	gcc -o ./bin/dll/selectionSort.dll -s --shared ./bin/o/selectionSort.o
	gcc -o ./bin/dll/timSort.dll -s --shared ./bin/o/timSort.o