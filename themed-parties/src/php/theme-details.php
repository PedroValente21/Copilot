<?php
// theme-details.php

// Sample data for themed parties
$themes = [
    1 => [
        'name' => 'Tropical Paradise',
        'description' => 'A vibrant tropical party with exotic decorations and fruity cocktails.',
        'date' => '2023-07-15',
        'image' => 'images/tropical.jpg'
    ],
    2 => [
        'name' => 'Retro 80s',
        'description' => 'A nostalgic party featuring 80s music, fashion, and arcade games.',
        'date' => '2023-08-20',
        'image' => 'images/retro.jpg'
    ],
    3 => [
        'name' => 'Masquerade Ball',
        'description' => 'An elegant evening with masks, formal attire, and a touch of mystery.',
        'date' => '2023-09-30',
        'image' => 'images/masquerade.jpg'
    ]
];

// Get the theme ID from the URL
$themeId = isset($_GET['id']) ? (int)$_GET['id'] : 1;

// Fetch the theme details
$theme = isset($themes[$themeId]) ? $themes[$themeId] : null;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/styles.css">
    <title><?php echo $theme ? $theme['name'] : 'Theme Not Found'; ?></title>
</head>
<body>
    <div class="theme-details">
        <?php if ($theme): ?>
            <h1><?php echo $theme['name']; ?></h1>
            <img src="<?php echo $theme['image']; ?>" alt="<?php echo $theme['name']; ?>">
            <p><?php echo $theme['description']; ?></p>
            <p>Date: <?php echo $theme['date']; ?></p>
        <?php else: ?>
            <h1>Theme Not Found</h1>
            <p>Sorry, we couldn't find the details for this theme.</p>
        <?php endif; ?>
    </div>
    <a href="index.php">Back to Home</a>
</body>
</html>