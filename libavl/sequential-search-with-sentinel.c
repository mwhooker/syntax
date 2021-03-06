/* Returns the smallest i such that array[i] == key, 
   or -1 if key is not in array[]. 
   array[] must be an modifiable array of n ints 
   with room for a (n + 1)th element. */
int 
seq_sentinel_search (int array[], int n, int key) 
{
  int *p;

  array[n] = key;
  for (p = array; *p != key; p++)
    /* Nothing to do. */;
  return p - array < n ? p - array : -1;
}
