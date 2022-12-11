#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct grade
{
    int number;
    char name[60];
    int math;
    int phy;
    int eng;
    int total;
}student[100];

int main()
{
    FILE *fp = fopen("stu.dat","r");
    int i,j;
	for(i=0;!feof(fp);i++)
    {
        fscanf(fp,"%d  %s  %d  %d  %d  %d",&student[i].number,student[i].name,&student[i].math,&student[i].phy,&student[i].eng,&student[i].total);
    }
    fclose(fp);
    
    struct grade change_student;
    printf("请输入要注销的学生学号");
	scanf("%d",&change_student.number);
    int a;
    for (a=0;a<i;a++)											//用学号做判据寻找要注销的学生信息 
    {
        if (student[a].number == change_student.number)					
      	{
      		int x;
			for(x=a;x<=i;x++)student[x]=student[x+1];          //student[i]中为0  0  0  0  0  0 
		}														
    }

    fopen("stu.dat","wb");
    for(j=0;j<i-1;j++)
    {
        fprintf(fp,"\n%d  %s  %d  %d  %d  %d",student[j].number,student[j].name,student[j].math,student[j].phy,student[j].eng,student[j].total);
    }
    printf("成绩信息注销成功\n"); 
	system("pause");
    fclose(fp);
    return 0;
}



