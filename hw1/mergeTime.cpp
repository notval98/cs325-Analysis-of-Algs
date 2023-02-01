#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <sstream>
#include <chrono>
using namespace std;
using namespace std::chrono;


void merge(vector<int> &data, int low, int high, int mid){
	// We have low to mid and mid+1 to high already sorted.
	int i, j, k, temp[high-low+1];
	i = low;
	k = 0;
	j = mid + 1;

	// merge the two parts into temp[].
	while (i <= mid && j <= high)
	{
		if (data[i] < data[j])
		{
			temp[k] = data[i];
			k++;
			i++;
		}
		else
		{
			temp[k] = data[j];
			k++;
			j++;
		}
	}

	// Insert all the remaining values from i to mid into temp[].
	while (i <= mid)
	{
		temp[k] = data[i];
		k++;
		i++;
	}

	// Insert all the remaining values from j to high into temp[].
	while (j <= high)
	{
		temp[k] = data[j];
		k++;
		j++;
	}
	
	// Assign sorted data stored in temp[] to a[].
	for (i = low; i <= high; i++)
	{
		data[i] = temp[i-low];
	}
}


void mergeSort(vector<int> &data, int low, int high){
int mid;
	if (low < high)
	{
		mid = (low+high) / 2;
		// Split the data into two half.
		mergeSort(data, low, mid);
		mergeSort(data, mid + 1, high);
		// merge them to get sorted output.
		merge(data, low, high, mid);
	}
}

int main(int argc, char *argv[]) {
	
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
		mergeSort(data, 0, data.size() - 1);
		clock_t end = clock();

		total_time = (end - start) /(float) CLOCKS_PER_SEC;
		cout << "Sorting Operation: " << operation << endl;
		cout << "Duration of algorithm in seconds: " << total_time << endl;
		operation++;
	}

	return 0;
}