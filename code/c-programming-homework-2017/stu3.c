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
    int i ,j;
    for(j=0;!feof(fp);j++)
    {
        fscanf(fp,"%d  %s  %d  %d  %d  %d",&student[j].number,student[j].name,&student[j].math,&student[j].phy,&student[j].eng,&student[j].total);
    }
    fclose(fp);
    int fin = 1;
	printf("请输入要查找的学生的学号：");
    scanf("%d",&fin);
    for(i = 0;i < j;i ++)
    {
        if (student[i].number == fin)
        	printf("%s同学的成绩为：\n数学：%d物理：%d 英语：%d 总分：%d\n",student[i].name,student[i].math,student[i].phy,student[i].eng,student[i].total);
    }
    system("pause");
    return 0;
}








