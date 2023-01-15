#!/usr/bin/env python3

class Person:
    
    def get_name(self):
        print("retrieving name")
        return self._name

    def set_name(self, name):
        if (type(name) is str and (1 <= len(name) <= 25)):
            print("setting name")
            title_cased = name.title()
            self._name = title_cased

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        print("retrieving job")
        return self._job

    def set_job(self, job):
        approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
        
        if(job in approved_jobs):
            print("setting job")
            self._job = job

        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name,)
    job = property(get_job, set_job,)