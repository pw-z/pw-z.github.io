#include <stdio.h>
//#include <string.h>
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
	FILE * fp1;	
	if ((fp1 = fopen("stu.dat","a")) == NULL)													
	{
		printf("文件打开失败\n");
	}
	else
	{
		int number,i,j;
	    printf("请输入要添加的学生成绩数目：");
	    scanf("%d",&number);
	    for(i=0;i<number;i++)
	    {
	    	printf("请输入学生学号:");
	        scanf("%d",&student[i].number);
	        printf("请输入学生姓名:");
	        scanf("%s",&student[i].name);
	        printf("请输入学生成绩(格式：数学 物理 英语 总分):");
	        scanf("%d %d %d %d",&student[i].math,&student[i].phy,&student[i].eng,&student[i].total);
	    }
	    for(j=0;j<i;j++)
	    {
	        fprintf(fp1,"\n%d  %s  %d  %d  %d  %d",student[j].number,student[j].name,student[j].math,student[j].phy,student[j].eng,student[j].total);
	    }
		printf("%d位同学的学生信息添加成功",number); 
	    fclose(fp1);
	}
	system("pause");
    return 0;
}
