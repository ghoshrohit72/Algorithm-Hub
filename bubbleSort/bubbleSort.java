public class bubbleSort
{
  float[] values;

void setup(){
size(800, 500);
values = new float[width];
for(int i=0;i<values.length;i++)
{
    values[i]=random(height);
}

//sorting Bubble sort
for (int i=0; i<values.length;i++){
  for(int j=0; j< values.length-i-1;j++){
    float a = values[j];
    float b = values[j+1];
    if(a > b)
    swap(values, j,j+1);
}
}
}

void draw()
{
background(0);
for(int i=0;i< values.length;i++)
{
    stroke(255);
    line(i, height,i, height - values[i]);
}
}

void swap(float[] arr, int i,int j){
  float tmp = arr[i];
  arr[i]=arr[j];
  arr[j]= tmp;
}}