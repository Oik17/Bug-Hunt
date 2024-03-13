#include <stdio.h>
#include <stdlib.h>

int firstMissingPositive(int* nums, int numsSize) {
  int i;

  for (i = 0; i < numsSize; ++i) {
    if (nums[i] <= 0) {
      nums[i] = numsSize + 1; 
    }
  }

  for (i = 0; i < numsSize; ++i) {
    int num = abs(nums[i]);
    if (num < numsSize) {
      nums[num - 1] = -abs(nums[num - 1]);
    }
  }

  for (i = numsSize - 1; i >= 0; --i) {
    if (nums[i] > 0) {
      return i + 1;
    }
  }

  return numsSize;
}

int main() {
  int nums[] = {3, 4, -1, 2, 1};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  printf("The smallest positive integer that is not present in nums is: %d\n", firstMissingPositive(nums, numsSize));
  return 0;
}
