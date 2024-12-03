using System;
using System.Collections;
using System.Collections.Generic;

class Student
{
    public string Name { get; set; }
    public int Age { get; set; }
    public double Grade { get; set; }

    public Student(string name, int age, double grade)
    {
        Name = name;
        Age = age;
        Grade = grade;
    }

    public override string ToString()
    {
        return $"{Name}, Age: {Age}, Grade: {Grade}";
    }
}

class StudentCollection : IEnumerable<Student>
{
    private List<Student> students = new List<Student>();

    public void Add(Student student)
    {
        students.Add(student);
    }

    public IEnumerator<Student> GetEnumerator()
    {
        return students.GetEnumerator();
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public IEnumerable<Student> FilterByGrade(double minGrade)
    {
        foreach (var student in students)
        {
            if (student.Grade >= minGrade)
            {
                yield return student;
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        var students = new StudentCollection();
        students.Add(new Student("Alice", 20, 4.5));
        students.Add(new Student("Bob", 22, 3.8));
        students.Add(new Student("Charlie", 19, 4.2));
        students.Add(new Student("Diana", 21, 3.5));

        Console.WriteLine("All students:");
        foreach (var student in students)
        {
            Console.WriteLine(student);
        }

        Console.WriteLine("\nStudents with grades >= 4.0:");
        foreach (var student in students.FilterByGrade(4.0))
        {
            Console.WriteLine(student);
        }
    }
}