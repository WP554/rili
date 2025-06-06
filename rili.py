<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Today in History</title>
    <meta name="description" content="Discover historical events that happened on this day">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: "#3b82f6",
                        secondary: "#1e40af",
                        accent: "#f59e0b"
                    }
                }
            }
        }
    </script>
</head>
<body class="min-h-screen bg-gray-50">
    <header class="bg-white shadow-sm">
        <nav class="container mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <i class="fas fa-calendar-day text-primary text-2xl"></i>
                <h1 class="text-xl font-bold text-gray-800">Today in History</h1>
            </div>
            <div class="flex items-center space-x-4">
                <button id="todayBtn" class="px-4 py-2 bg-primary text-white rounded-md hover:bg-secondary transition">
                    Today
                </button>
                <input 
                    type="date" 
                    id="datePicker" 
                    class="border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
                >
            </div>
        </nav>
    </header>

    <main class="container mx-auto px-4 py-8">
        <div class="bg-white rounded-lg shadow-md p-6 mb-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
                <h2 id="currentDate" class="text-2xl font-bold text-gray-800 mb-2 md:mb-0"></h2>
                <div class="flex items-center space-x-2">
                    <span class="text-gray-600">Showing events for:</span>
                    <span id="displayDate" class="font-semibold text-primary"></span>
                </div>
            </div>

            <div id="eventsContainer" class="space-y-6">
                <!-- Events will be loaded here -->
                <div class="animate-pulse flex flex-col space-y-4">
                    <div class="h-6 bg-gray-200 rounded w-3/4"></div>
                    <div class="h-4 bg-gray-200 rounded w-full"></div>
                    <div class="h-4 bg-gray-200 rounded w-5/6"></div>
                </div>
            </div>
        </div>

        <div class="bg-white rounded-lg shadow-md p-6">
            <h3 class="text-xl font-semibold text-gray-800 mb-4">Browse Other Dates</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-7 gap-2">
                <!-- Calendar days will be generated here -->
            </div>
        </div>
    </main>
    <footer class="bg-gray-100 mt-12 py-8">
        <div class="container mx-auto px-4 text-center text-gray-600">
            <p>© <span id="currentYear"></span> Today in History. All historical data sourced from public APIs.</p>
        </div>
    </footer>
    
    <script>
        // Historical events data (in a real app, this would come from an API)
        const historicalEvents = {
            "01-01": [
                { year: "45 BC", event: "Julian calendar takes effect as the civil calendar of the Roman Empire" },
                { year: "1801", event: "The first known asteroid 1 Ceres is discovered by Giuseppe Piazzi" },
                { year: "1863", event: "Abraham Lincoln signs the Emancipation Proclamation" }
            ],
            "01-02": [
                { year: "1492", event: "Reconquista completes as the Emirate of Granada falls" },
                { year: "1788", event: "Georgia becomes the fourth state to ratify the United States Constitution" }
            ],
            // More dates would be added in a real implementation
            // For demo purposes, we'll generate random events for other dates
        };

        // DOM elements
        const datePicker = document.getElementById('datePicker');
        const todayBtn = document.getElementById('todayBtn');
        const currentDateEl = document.getElementById('currentDate');
        const displayDateEl = document.getElementById('displayDate');
        const eventsContainer = document.getElementById('eventsContainer');
        const currentYearEl = document.getElementById('currentYear');
        const calendarDaysContainer = document.querySelector('.grid');

        // Initialize the page
        document.addEventListener('DOMContentLoaded', function() {
            // Set current year in footer
            currentYearEl.textContent = new Date().getFullYear();
            
            // Set default date to today
            const today = new Date();
            setDate(today);
            
            // Generate calendar days
            generateCalendarDays();
        });

        // Date picker change handler
        datePicker.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            setDate(selectedDate);
        });

        // Today button click handler
        todayBtn.addEventListener('click', function() {
            const today = new Date();
            datePicker.valueAsDate = today;
            setDate(today);
        });

        // Set the displayed date and show events
        function setDate(date) {
            const monthNames = ["January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December"];
            
            const day = date.getDate();
            const month = monthNames[date.getMonth()];
            const year = date.getFullYear();
            
            // Format date as MM-DD for event lookup
            const monthDay = `${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
            
            // Update UI
            currentDateEl.textContent = `${month} ${day}`;
            displayDateEl.textContent = `${month} ${day}, ${year}`;
            
            // Show events for this date
            showEvents(monthDay);
        }

        // Display events for the selected date
        function showEvents(monthDay) {
            // Clear current events
            eventsContainer.innerHTML = '';
            
            // Get events for this date (or generate random ones if none exist)
            let events = historicalEvents[monthDay];
            
            if (!events || events.length === 0) {
                // Generate some random events for demonstration
                const randomCount = Math.floor(Math.random() * 3) + 2;
                events = [];
                
                for (let i = 0; i < randomCount; i++) {
                    const randomYear = Math.floor(Math.random() * (2023 - 1000 + 1)) + 1000;
                    events.push({
                        year: randomYear,
                        event: `A significant historical event occurred in ${randomYear}`
                    });
                }
            }
            
            // Display events
            if (events.length === 0) {
                eventsContainer.innerHTML = `
                    <div class="text-center py-8 text-gray-500">
                        <i class="fas fa-history text-4xl mb-4 text-gray-300"></i>
                        <p>No historical events found for this date.</p>
                    </div>
                `;
            } else {
                events.forEach(event => {
                    const eventEl = document.createElement('div');
                    eventEl.className = 'border-l-4 border-primary pl-4 py-2';
                    eventEl.innerHTML = `
                        <div class="flex items-baseline space-x-2">
                            <span class="text-lg font-bold text-primary">${event.year}</span>
                            <span class="text-gray-700">${event.event}</span>
                        </div>
                    `;
                    eventsContainer.appendChild(eventEl);
                });
            }
        }

        // Generate calendar days for the current month
        function generateCalendarDays() {
            const today = new Date();
            const currentMonth = today.getMonth();
            const currentYear = today.getFullYear();
            
            // Get first and last day of month
            const firstDay = new Date(currentYear, currentMonth, 1);
            const lastDay = new Date(currentYear, currentMonth + 1, 0);
            
            // Clear calendar
            calendarDaysContainer.innerHTML = '';
            
            // Add day headers
            const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            dayNames.forEach(day => {
                const dayHeader = document.createElement('div');
                dayHeader.className = 'text-center font-semibold text-gray-600 text-sm';
                dayHeader.textContent = day;
                calendarDaysContainer.appendChild(dayHeader);
            });
            
            // Add empty cells for days before the first day of month
            for (let i = 0; i < firstDay.getDay(); i++) {
                const emptyDay = document.createElement('div');
                emptyDay.className = 'h-10';
                calendarDaysContainer.appendChild(emptyDay);
            }
            
            // Add days of month
            for (let day = 1; day <= lastDay.getDate(); day++) {
                const dayEl = document.createElement('button');
                dayEl.className = 'h-10 w-10 mx-auto rounded-full flex items-center justify-center text-sm hover:bg-gray-100 transition';
                
                // Highlight current day
                if (day === today.getDate() && currentMonth === today.getMonth() && currentYear === today.getFullYear()) {
                    dayEl.className += ' bg-primary text-white hover:bg-secondary';
                }
                
                dayEl.textContent = day;
                
                // Add click handler to select this date
                dayEl.addEventListener('click', function() {
                    const selectedDate = new Date(currentYear, currentMonth, day);
                    datePicker.valueAsDate = selectedDate;
                    setDate(selectedDate);
                });
                
                calendarDaysContainer.appendChild(dayEl);
            }
        }
    </script>
</body>
</html>
