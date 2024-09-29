from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm, WorkExperienceForm, EducationForm, CertificationForm, ProjectForm
from .models import UserProfile, WorkExperience, Education, Certification, Project

# View for displaying and editing user profile
def profile_view(request):
    # Assume a default user or use some identifier (e.g., session or default user ID)
    profile, created = UserProfile.objects.get_or_create(id=1)  # Replace '1' with actual logic if needed
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile_view.html', {'profile': profile, 'user': profile.user})

# View for editing or creating user profile
def edit_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(id=1)  # Replace '1' with actual logic if needed

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

# View for displaying the user's portfolio
def portfolio_view(request):
    profile, created = UserProfile.objects.get_or_create(id=1)  # Replace '1' with actual logic if needed

    work_experiences = WorkExperience.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    certifications = Certification.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)

    return render(request, 'portfolio_view.html', {
        'profile': profile,
        'work_experiences': work_experiences,
        'educations': educations,
        'certifications': certifications,
        'projects': projects,
    })

# View for adding work experience
def add_work_experience(request):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.profile = profile
            work_experience.save()
            return redirect('portfolio_view')
    else:
        form = WorkExperienceForm()
    return render(request, 'add_work_experience.html', {'form': form})

# View for editing work experience
def edit_work_experience(request, pk):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    work_experience = get_object_or_404(WorkExperience, pk=pk, profile=profile)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('portfolio_view')
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'edit_work_experience.html', {'form': form})

# View for adding education
def add_education(request):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.profile = profile
            education.save()
            return redirect('portfolio_view')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})

# View for editing education
def edit_education(request, pk):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    education = get_object_or_404(Education, pk=pk, profile=profile)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('portfolio_view')
    else:
        form = EducationForm(instance=education)
    return render(request, 'edit_education.html', {'form': form})

# View for adding certification
def add_certification(request):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.profile = profile
            certification.save()
            return redirect('portfolio_view')
    else:
        form = CertificationForm()
    return render(request, 'add_certification.html', {'form': form})

# View for editing certification
def edit_certification(request, pk):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    certification = get_object_or_404(Certification, pk=pk, profile=profile)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('portfolio_view')
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'edit_certification.html', {'form': form})

# View for adding a project
def add_project_view(request):
    profile = UserProfile.objects.get(id=1)  # Replace '1' with actual logic if needed
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile
            project.save()
            return redirect('portfolio_view')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# View for editing a project
def edit_project_view(request, project_id):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    project = get_object_or_404(Project, id=project_id, profile=profile)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio_view')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

# View for deleting a project
def delete_project_view(request, project_id):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    project = get_object_or_404(Project, id=project_id, profile=profile)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_view')
    return render(request, 'delete_project.html', {'project': project})

# View for showcasing projects
def showcase_view(request):
    profile = get_object_or_404(UserProfile, id=1)  # Replace '1' with actual logic if needed
    projects = Project.objects.filter(profile=profile)
    return render(request, 'showcase.html', {'projects': projects})
