all: create, compile, link

create:
	mkdir -p ./bin/dll
	mkdir -p ./bin/o

compile:
	gcc -o ./bin/o/bubbleSort.o -c ./src/c/bubbleSort.c
	gcc -o ./bin/o/doubleSelectionSort.o -c ./src/c/doubleSelectionSort.c
	gcc -o ./bin/o/heapSort.o -c ./src/c/heapSort.c
	gcc -o ./bin/o/insertionSort.o -c ./src/c/insertionSort.c
	gcc -o ./bin/o/mergeSort.o -c ./src/c/mergeSort.c
	gcc -o ./bin/o/quickSort.o -c ./src/c/quickSort.c
	gcc -o ./bin/o/reverseSelectionSort.o -c ./src/c/reverseSelectionSort.c
	gcc -o ./bin/o/selectionSort.o -c ./src/c/selectionSort.c

link:
	gcc -o./bin/dll/bubbleSort.dll -s --shared ./bin/o/bubbleSort.o
	gcc -o./bin/dll/doubleSelectionSort.dll -s --shared ./bin/o/doubleSelectionSort.o
	gcc -o./bin/dll/heapSort.dll -s --shared ./bin/o/heapSort.o
	gcc -o./bin/dll/insertionSort.dll -s --shared ./bin/o/insertionSort.o
	gcc -o./bin/dll/mergeSort.dll -s --shared ./bin/o/mergeSort.o
	gcc -o./bin/dll/quickSort.dll -s --shared ./bin/o/quickSort.o
	gcc -o./bin/dll/reverseSelectionSort.dll -s --shared ./bin/o/reverseSelectionSort.o
	gcc -o./bin/dll/selectionSort.dll -s --shared ./bin/o/selectionSort.o