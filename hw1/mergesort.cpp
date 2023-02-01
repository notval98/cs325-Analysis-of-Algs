#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

// A function to merge the two half into a sorted data.
void merge(vector<int> &data, int low, int high, int mid)
{
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

// A function to split array into two parts.
void mergeSort(vector<int> &data, int low, int high)
{
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

int main()
{

	vector<int> data;
	ifstream input_file;
	ofstream output_file;

	input_file.open("data.txt");

	if (input_file.is_open()) 
	{
		int val;
		while (!input_file.eof()) 
		{
			input_file >> val;
			data.push_back(val);
		}

		input_file.close();

		mergeSort(data, 0, data.size() - 1);

		output_file.open("insert.txt");

		for (int i = 0; i < data.size(); i++) 
		{
			output_file << data[i];
			output_file << " ";
		}

		output_file.close();
		cout << "data.txt read, values sorted and stored in insert.txt" << endl;
	}

	else 
	{
		cout << "File was not openned." << endl;
	}
	
	return 0;
}