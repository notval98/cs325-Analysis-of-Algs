#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <sstream>
#include <chrono>
using namespace std;
using namespace std::chrono;


void insertsort(vector<int> &data, int num_elements) 
{
	int i, j, key;

		for (int i = 1; i < data.size(); i++)
		{
			key = data[i]; //picking next element
			j = i - 1;

			/* Move elements of arr[0..i-1], that are 
     	   	greater than key, to one position ahead 
       		of their current position */
			while (j >= 0 && data[j] > key)
			{
				data[j + 1] = data[j];
				j = j - 1;
			}

			data[j + 1] = key;
		}
}


int main(int argc, char *argv[]) 
{

	vector<int> data;
	int random_num, num_elements;
	clock_t start, end;
	float total_time;
	int operation = 1;

	for(int i = 5000; i <= 50000; i+= 5000)
	{
	
		for (int j = 0; j < i; j++) 
		{
			int random_num = rand() % 10000 + 1;
			data.push_back(random_num);
			num_elements++;
		}

		clock_t start = clock();
		insertsort(data, num_elements);
		clock_t end = clock();

		total_time = (end - start) /(float) CLOCKS_PER_SEC;
		cout << "Sorting Operation: " << operation << endl;
		cout << "Duration of algorithm in seconds: " << total_time << endl;
		operation++;
	}
	
	return 0;
}