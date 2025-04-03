function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            document.getElementById('location').value = 
                `${position.coords.latitude}, ${position.coords.longitude}`;
        });
    }
}

function toggleAge(button, value) {
    // Remove active class from all buttons
    document.querySelectorAll('.age-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Add active class to clicked button
    button.classList.add('active');
    
    // Update the hidden select field
    const selectField = document.getElementById('age_group');
    selectField.value = value;
}

function addPerson() {
    const newForm = document.querySelector('.form-section').cloneNode(true);
    document.querySelector('.form-container').appendChild(newForm);
}

function toggleNews() {
    const newsSection = document.querySelector('.news-section');
    newsSection.classList.toggle('expanded');
}

// async function submitForm() {
//     const form = document.getElementById('reportForm');
//     const formData = new FormData(form);

//     // Add dynamic fields
//     const ageGroup = document.querySelector('.age-btn.active')?.dataset.value;
//     if (ageGroup) formData.append('age_group', ageGroup);

//     try {
//         const response = await fetch(form.action, {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'Accept': 'application/json',
//             }
//         });

//         // Check if response is JSON
//         const contentType = response.headers.get('content-type');
//         if (!contentType || !contentType.includes('application/json')) {
//             throw new Error('Server did not return JSON');
//         }

//         const result = await response.json();

//         if (response.ok) {
//             alert(result.message || 'Report submitted successfully!');
//             form.reset(); // Optional: Clear the form
//         } else {
//             // Handle validation errors
//             if (result.errors) {
//                 const errorMessages = Object.values(result.errors).join(', ');
//                 alert(`Validation errors: ${errorMessages}`);
//             } else {
//                 alert(result.error || 'Submission failed');
//             }
//         }
//     } catch (error) {
//         console.error('Submission failed:', error);
//         alert('Failed to submit form. Please try again.');
//     }
// }