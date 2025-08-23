from django.db import models
#from exams.models import Exam #needed for direct access e.g exam = Exam.objects.get(name="End-Term 1", academic_year="2025", term="2025 T1"), exam.results.all()
# from datetime import datetime
from django.utils import timezone
import uuid

#funtion to generate random but different result ids
def generate_unique_result_id():
    #from results.models import Result #commented out since are in same file
    while True:
        new_id = f"RES-{uuid.uuid4().hex[:8].upper()}"
        if not Result.objects.filter(result_id=new_id).exists():
            return new_id

# Create your models here.
class Result(models.Model):
    #1. random and unpredicatble result id but different for everyone
    result_id = models.CharField(primary_key=True,max_length=20, default=generate_unique_result_id, help_text="unique and unpreictable result id for results")
    #2. foreign keys for student,subject,class and teacher
    result_student = models.ForeignKey('students.Student', to_field='student_id', on_delete=models.CASCADE, related_name='results', help_text="The student this result belongs to.")
    result_subject = models.ForeignKey('subjects.Subject', to_field='subject_id', on_delete=models.CASCADE, related_name='results', help_text="The subject being assessed.")
    result_class = models.ForeignKey('classes.SchoolClass', to_field='class_id', on_delete=models.SET_NULL, null=True, blank=True, related_name='results', help_text="The class for which this result was recorded.")
    result_teacher = models.ForeignKey('teachers.Teacher', to_field='teacher_id', on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_results', help_text="Teacher who graded or recorded the result.")
    #3. Exam Type --.to be changed for links with exam
    # RESULT_TYPE_CHOICES = [ ('Assignment', 'Assignment'), ('CAT', 'CAT'),
    #     ('Pre-lim', 'Pre-lim'),
    #     ('Mid-Term', 'Mid-Term'),
    #     ('End-Term', 'End-Term'),
    #     ('Project', 'Project'),
    #     ('Zonal Exam', 'Zonal Exam'),
    #     ('Other', 'Other'),
    # ] 
    # result_exam_type = models.CharField(max_length=20, choices=RESULT_TYPE_CHOICES, default='CAT', help_text="Type of exam")
    result_exam = models.ForeignKey('exams.Exam', to_field='exam_id',null=True, on_delete=models.CASCADE, related_name='results', help_text="The result this exam belongs to")
    #4. exam term and academin year
    # RESULT_TERM_CHOICES = [('Term-1','Term-1'),('Term-2','Term-2'),('Term-3','Term-3'), ]
    # result_term = models.CharField(max_length=20,choices=RESULT_TERM_CHOICES, help_text="Academic term when the exam was done")
    # result_year = models.IntegerField(default=datetime.now().year, help_text="Year done e.g. 2025")
    #5. student perfomance 
    result_score = models.DecimalField(max_digits=4, decimal_places=2, help_text="Numeric score e.g 99.99")
    result_grade = models.CharField(max_length=5, null=True, blank=True, help_text="Grade Awarded e.g EE1")
    result_remarks = models.TextField(null=True, blank=True, help_text="Teachers comments")
    #6. Timestamps to record when last updated
    result_creation_date = models.DateTimeField(default=timezone.now, help_text="When the result was first recorded")
    results_update_date = models.DateTimeField(auto_now=True, help_text="Last time the record was updated")

    #7. String representation of the results
    def __str__(self):
        return f"{self.result_student} | {self.result_subject.subject_name} | {self.result_exam.exam_term} {self.result_exam.exam_year}"
    #8. Meta ordering
    class Meta:
        unique_together = ('result_exam', 'result_student', 'result_subject')
        ordering = ['-result_creation_date']

