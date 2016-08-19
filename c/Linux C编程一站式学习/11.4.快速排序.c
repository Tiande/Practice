#include <stdio.h>

#define LEN 8
int a[LEN] = { 5, 2, 4, 7, 1, 3, 2, 6}; 

int partition(int start, int end)
{
    int pivot = a[end];
    while (start < end) {
        while (start<end && a[start]<=pivot) {
            ++start;
        }
        a[end] = a[start];
        while (start<end && a[end]>=pivot){
            --end;
        }
        a[start] = a[end];
    }
    a[start] = pivot;
    return start;
}

void quicksort(int start, int end)
{
    int mid;
    if (end > start) {
        mid = partition(start, end);
        printf("start: %d %d %d %d %d %d %d %d\n",
                a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]);
        quicksort(start, mid-1);
        /* quicksort(mid+1, end); */
        printf("end: %d %d %d %d %d %d %d %d\n",
                a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]);
    }
}

int main(void)
{
    quicksort(0, LEN-1);

    return 0;
}
