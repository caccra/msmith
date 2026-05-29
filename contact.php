<?php
header('Content-Type: application/json');
header('X-Content-Type-Options: nosniff');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

// Honeypot — bots fill this, humans don't
if (!empty($_POST['website'])) {
    echo json_encode(['success' => true]);
    exit;
}

function clean(string $str): string {
    return htmlspecialchars(strip_tags(trim($str)), ENT_QUOTES, 'UTF-8');
}

$name    = clean($_POST['name']    ?? '');
$email   = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$phone   = clean($_POST['phone']   ?? '');
$service = clean($_POST['service'] ?? '');
$message = clean($_POST['message'] ?? '');

if (!$name || !$email || !$message) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Please fill in your name, email, and message.']);
    exit;
}

$to      = 'info@m-smithadvocates.com';
$subject = '=?UTF-8?B?' . base64_encode('New Enquiry from ' . $name . ' — M-Smith Advocates') . '?=';

$body  = "New enquiry from the M-Smith Advocates website.\n\n";
$body .= "Name:          " . $name    . "\n";
$body .= "Email:         " . $email   . "\n";
$body .= "Phone:         " . ($phone   ?: 'Not provided') . "\n";
$body .= "Practice area: " . ($service ?: 'Not specified') . "\n\n";
$body .= "Message:\n" . wordwrap($message, 72, "\n", false) . "\n\n";
$body .= "---\nSent via the contact form at m-smithadvocates.com";

$headers  = "From: M-Smith Advocates <info@m-smithadvocates.com>\r\n";
$headers .= "Reply-To: " . $name . " <" . $email . ">\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "Content-Transfer-Encoding: 8bit\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

$sent = mail($to, $subject, $body, $headers, '-f info@m-smithadvocates.com');

if ($sent) {
    echo json_encode(['success' => true]);
} else {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error'   => 'Message could not be delivered. Please email us directly at info@m-smithadvocates.com.'
    ]);
}
