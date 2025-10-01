from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from portfolio.models import Profile, Experience, Skill, Education, Certification, Project, Recommendation

class Command(BaseCommand):
    help = 'Populate database with dummy portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Creating dummy portfolio data...')
        
        # Clear existing data
        Profile.objects.all().delete()
        Experience.objects.all().delete()
        Skill.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Project.objects.all().delete()
        Recommendation.objects.all().delete()
        
        # Create Profile
        profile = Profile.objects.create(
            name="Nantalira Niar Wijaya",
            title="Software Developer",
            summary="A backend-focused Software Developer with 2+ years of experience in designing clean and efficient system architectures. Highly experienced in collaborating with frontend and design teams to define robust system flows and API contracts. As an adaptive learner, I am adept at selecting and mastering the most appropriate technologies to solve a problem, rather than being limited to a single toolset.",
            email="nantalirawijaya@gmail.com",
            linkedin="https://www.linkedin.com/in/nantalira/",
            github="https://github.com/nantalira"
        )
        
        # Create Experiences
        Experience.objects.create(
            title="Junior Programmer",
            company="CV Hexanindo Pratama",
            location="Semarang, Indonesia",
            start_date=date(2024, 2, 1),
            end_date=date(2025, 7, 30),
            job_list="Initiated the development of a new version of the \"de BeTaPa\" management system for the Indonesian Ministry of Agriculture, designed to enhance the functionality of the legacy system.\nHeld full responsibility for the development lifecycle, from database design and RESTful API creation to testing with Docker.\nSuccessfully launched a more complex application that resolved key shortcomings of the previous system and streamlined user workflows for better efficiency."
        )
        
        Experience.objects.create(
            title="Fullstack Web Developer",
            company="Freelance",
            location="Remote",
            start_date=date(2023, 6, 1),
            end_date=date(2024, 1, 30),
            job_list="Undertook and executed various independent web development projects for small-scale clients, focusing on creating functional, needs-based websites.\nManaged the entire project pipeline, from understanding client requirements and development to final project delivery.\nConsistently delivered reliable web solutions that successfully met all client specifications on schedule."
        )
        
        Experience.objects.create(
            title="Backend Engineer Intern",
            company="PT Stechoq Robotika Indonesia",
            location="Yogyakarta, Indonesia",
            start_date=date(2023, 2, 1),
            end_date=date(2023, 6, 30),
            job_list="Contributed as a core backend engineer during the initialization phase of the \"Beliternak\" application, a livestock marketplace platform and Assisted on other team projects, including the \"Dashboard Goat Milk Monitoring\" application for monitoring dairy goats' progress at Sembada Farm\nDesigned the initial database schema and built and documented a set of core APIs  that served as the foundation for the entire application.\nSuccessfully established a solid and well-documented backend foundation, which enabled the web and mobile frontend teams to smoothly begin their development and integration process."
        )
        Experience.objects.create(
            title="Research Group for Human Robot Interaction",
            company="SOFOSTROBOTICS.ID",
            location="Yogyakarta, Indonesia",
            start_date=date(2022, 10, 1),
            end_date=date(2023, 2, 28),
            job_list="Create a chatbot with the Rasa framework for \"Companion Robot for Elder People\".\nCreate a knowledge base based on research in nursing homes."
        )
        
        # Create Skills
        skills_data = [
            ('Laravel', 'programming'),
            ('Express.js', 'programming'),
            ('Django', 'programming'),
            ('React', 'programming'),
            ('MySQL', 'database'),
            ('PostgreSQL', 'database'),
            ('SQL', 'database'),
            ('Object Relational Mapping (Sequelize, Laravel Eloquent)', 'database'),
            ('Docker', 'devops'),
            ('Git', 'devops'),
            ('GitHub', 'devops'),
            ('GitLab', 'devops'),
            ('Problem solving', 'soft'),
            ('Critical thinking', 'soft'),
            ('Time management', 'soft'),
            ('Adaptability', 'soft'),
            ('Collaboration', 'soft'),
            ('Communication', 'soft'),
        ]
        
        for name, skill_type in skills_data:
            Skill.objects.create(name=name, type=skill_type)
        
        # Create Education
        Education.objects.create(
            degree="Bachelor of Information Technology",
            institution="Dian Nuswantoro University",
            location="Semarang, Indonesia",
            start_date=date(2020, 9, 1),
            graduation_date=date(2024, 5, 15),
            gpa=3.84,
            thesis_name="Music-Genre Classification using Bidirectional Long Short- Term Memory and Mel-Frequency Cepstral Coefficients",
            thesis_url="https://www.researchgate.net/publication/378000109_Music-Genre_Classification_using_Bidirectional_Long_Short-_Term_Memory_and_Mel-Frequency_Cepstral_Coefficients"
        )
        
        # Create Certifications
        Certification.objects.create(
            name="Meta Back-End Developer",
            issuer="Meta",
            issue_date=date(2025, 9, 23),
            certificate_url="https://www.coursera.org/account/accomplishments/specialization/I8TD9U8DNLRL",
        )

        Certification.objects.create(
            name="Certification Scheme of Web Developer",
            issuer="Badan Nasional Sertifikasi Profesi (BNSP)",
            issue_date=date(2024, 4, 22),
            expiry_date=date(2028, 2, 23),
            certificate_url="",
        )

        Certification.objects.create(
            name="Artificial Intelligence BIZ",
            issuer="CertNexus",
            issue_date=date(2023, 2, 23),
            certificate_url="https://www.credential.net/3956908a-6c87-45ac-8c8d-a25f632a781a#acc.46zXivdT",
        )
        
        # Create Projects
        Project.objects.create(
            title="Portfolio Website",
            technologies="Django, Bootstrap, HTML5, CSS3",
            live_url="https://alexandra-moore.com",
            github_url="https://github.com/alexandra/portfolio",
            key_achievements="Personal portfolio website showcasing creative work and production capabilities.\nBuilt with modern web technologies and responsive design principles.\nFeatures dark theme design and smooth scroll interactions for optimal user experience."
        )
        # Create Recommendations
        Recommendation.objects.create(
            name="Client",
            title="Brand Director", 
            company="Driftwell",
            text="Alexandra brings sunshine to creative teams. Her optimism, problem-solving, and clear communication drive success."
        )
        
        Recommendation.objects.create(
            name="Creative Director",
            title="Creative Director",
            company="Creative Agency XYZ", 
            text="Alexandra is hungry to tackle new challenges. She's delightful with clients and can diffuse a tense room with her laugh."
        )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created dummy portfolio data!')
        )
        self.stdout.write(f'Created:')
        self.stdout.write(f'  - 1 Profile')
        self.stdout.write(f'  - {Experience.objects.count()} Experiences')
        self.stdout.write(f'  - {Skill.objects.count()} Skills')
        self.stdout.write(f'  - {Education.objects.count()} Education records')
        self.stdout.write(f'  - {Certification.objects.count()} Certifications')
        self.stdout.write(f'  - {Project.objects.count()} Projects')
        self.stdout.write(f'  - {Recommendation.objects.count()} Recommendations')