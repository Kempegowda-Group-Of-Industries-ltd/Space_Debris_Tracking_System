// setup_spacedebris.js

// Switch to the spacedebris database
use spacedebris;

// Insert sample debris data
db.debris.insertMany([
    { name: "Debris A", size: 10, mass: 500, currentOrbit: "LEO", trajectoryData: {}, lastUpdated: new Date() },
    { name: "Debris B", size: 5, mass: 300, currentOrbit: "MEO", trajectoryData: {}, lastUpdated: new Date() }
]);

print("Sample data inserted into the spacedebris database.");
