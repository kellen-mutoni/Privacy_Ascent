-- Sample Resources for Privacy Ascent Mental Health Application
-- Run this file to populate the resources table with helpful mental health resources

USE privacy_ascent;

-- Clear existing resources (optional - remove this line if you want to keep existing data)
-- DELETE FROM resources;

-- Crisis Support Resources
INSERT INTO resources (title, category, content) VALUES
('National Suicide Prevention Lifeline', 'Crisis Support', 'Available 24/7 at 988 or 1-800-273-8255. Free and confidential support for people in distress.'),
('Crisis Text Line', 'Crisis Support', 'Text HOME to 741741 to connect with a Crisis Counselor. Free 24/7 support via text message.'),
('SAMHSA National Helpline', 'Crisis Support', 'Call 1-800-662-4357 for free, confidential, 24/7 treatment referral and information service.'),
('International Association for Suicide Prevention', 'Crisis Support', 'Visit iasp.info/resources/Crisis_Centres for crisis centers worldwide.');

-- Anxiety Management Resources
INSERT INTO resources (title, category, content) VALUES
('Deep Breathing Exercise', 'Anxiety Management', 'Try the 4-7-8 technique: Breathe in for 4 counts, hold for 7, exhale for 8. Repeat 4 times.'),
('Grounding Technique: 5-4-3-2-1', 'Anxiety Management', 'Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, and 1 you taste.'),
('Progressive Muscle Relaxation', 'Anxiety Management', 'Tense and relax each muscle group starting from your toes up to your head.'),
('Anxiety and Depression Association', 'Anxiety Management', 'Visit adaa.org for evidence-based resources, self-help tools, and professional support information.');

-- Depression Support Resources
INSERT INTO resources (title, category, content) VALUES
('Understanding Depression', 'Depression Support', 'Depression is a medical condition, not a weakness. It affects how you feel, think, and handle daily activities.'),
('Daily Self-Care Checklist', 'Depression Support', 'Small steps matter: Get sunlight, eat regular meals, stay hydrated, move your body, and reach out to someone.'),
('NAMI - National Alliance on Mental Illness', 'Depression Support', 'Visit nami.org or call 1-800-950-6264 for education, support groups, and advocacy resources.'),
('Depression and Bipolar Support Alliance', 'Depression Support', 'Visit dbsalliance.org for peer support groups, educational resources, and wellness tools.');

-- Stress Management Resources
INSERT INTO resources (title, category, content) VALUES
('Time Management Tips', 'Stress Management', 'Break tasks into smaller steps, prioritize what matters most, and schedule breaks throughout your day.'),
('Mindfulness Meditation', 'Stress Management', 'Spend 5-10 minutes focusing on your breath. When your mind wanders, gently bring it back without judgment.'),
('Physical Activity for Stress', 'Stress Management', 'Even 10 minutes of walking can reduce stress hormones and boost mood-enhancing endorphins.'),
('Setting Healthy Boundaries', 'Stress Management', 'Learn to say no, communicate your limits clearly, and prioritize your well-being without guilt.');

-- Self-Care Resources
INSERT INTO resources (title, category, content) VALUES
('Sleep Hygiene Tips', 'Self-Care', 'Maintain a regular sleep schedule, avoid screens 1 hour before bed, and create a cool, dark sleeping environment.'),
('Nutrition and Mental Health', 'Self-Care', 'Eat regular balanced meals with whole grains, fruits, vegetables, and lean proteins. Stay hydrated.'),
('Social Connection', 'Self-Care', 'Reach out to friends or family, join a support group, or volunteer. Connection is vital for mental health.'),
('Journaling for Mental Health', 'Self-Care', 'Write about your thoughts and feelings daily. It can help process emotions and identify patterns.');

-- Trauma Support Resources
INSERT INTO resources (title, category, content) VALUES
('RAINN - Rape, Abuse & Incest National Network', 'Trauma Support', 'Call 1-800-656-4673 or visit rainn.org for confidential support from trained staff members.'),
('National Domestic Violence Hotline', 'Trauma Support', 'Call 1-800-799-7233 or text START to 88788. Available 24/7 for support and resources.'),
('Understanding PTSD', 'Trauma Support', 'Post-traumatic stress is a normal response to abnormal events. Professional help can make a significant difference.'),
('Trauma-Informed Self-Care', 'Trauma Support', 'Be patient with yourself, establish safety and routine, and seek professional support when ready.');

-- Professional Help Resources
INSERT INTO resources (title, category, content) VALUES
('Finding a Therapist', 'Professional Help', 'Psychology Today (psychologytoday.com) offers a therapist directory searchable by location, insurance, and specialty.'),
('Teletherapy Options', 'Professional Help', 'BetterHelp, Talkspace, and many local providers offer online therapy sessions for accessibility and convenience.'),
('When to Seek Emergency Help', 'Professional Help', 'If you are in immediate danger or having thoughts of harming yourself or others, call 911 or go to the nearest ER.'),
('Community Mental Health Centers', 'Professional Help', 'SAMHSA Treatment Locator at findtreatment.gov helps find affordable mental health services in your area.');

-- Mindfulness and Meditation Resources
INSERT INTO resources (title, category, content) VALUES
('Beginner Meditation Guide', 'Mindfulness', 'Start with 2-5 minutes daily. Sit comfortably, focus on your breath, and observe thoughts without judgment.'),
('Body Scan Meditation', 'Mindfulness', 'Lie down and mentally scan your body from head to toe, noticing sensations without trying to change them.'),
('Mindful Walking', 'Mindfulness', 'Walk slowly and deliberately, paying attention to each step, your breathing, and the environment around you.'),
('Free Meditation Apps', 'Mindfulness', 'Try Insight Timer, UCLA Mindful, or Smiling Mind for guided meditations and mindfulness exercises.');

-- Relationship and Social Support Resources
INSERT INTO resources (title, category, content) VALUES
('Healthy Communication Skills', 'Relationships', 'Use I-statements, listen actively, validate feelings, and address issues calmly without blame.'),
('Recognizing Toxic Relationships', 'Relationships', 'Warning signs include manipulation, constant criticism, isolation from others, and disrespect for boundaries.'),
('Building Support Networks', 'Relationships', 'Join clubs, attend community events, volunteer, or participate in online communities with shared interests.'),
('Family Support Resources', 'Relationships', 'Al-Anon and Nar-Anon offer support for families affected by addiction. NAMI offers family support groups.');

-- Workplace Mental Health Resources
INSERT INTO resources (title, category, content) VALUES
('Managing Work Stress', 'Workplace Wellness', 'Take regular breaks, set realistic goals, communicate with supervisors, and separate work from personal time.'),
('Employee Assistance Programs', 'Workplace Wellness', 'Many employers offer free confidential counseling. Check with HR about available EAP services.'),
('Work-Life Balance', 'Workplace Wellness', 'Set boundaries between work and home, schedule personal time, and prioritize activities that recharge you.'),
('Burnout Prevention', 'Workplace Wellness', 'Recognize early signs: exhaustion, cynicism, reduced performance. Take action before burnout becomes severe.');

-- Youth Mental Health Resources
INSERT INTO resources (title, category, content) VALUES
('Teen Line', 'Youth Support', 'Call 1-800-852-8336 or text TEEN to 839863. Teens helping teens, available 6pm-10pm PT daily.'),
('The Trevor Project', 'Youth Support', 'Call 1-866-488-7386 or text START to 678678. Crisis support for LGBTQ+ youth available 24/7.'),
('School Counseling Resources', 'Youth Support', 'Talk to your school counselor, nurse, or trusted teacher. They can connect you with appropriate support.'),
('Youth Mental Health First Aid', 'Youth Support', 'Learn to recognize signs of mental health challenges in yourself and friends. Visit mhfa.org for resources.');

-- Positive Psychology Resources
INSERT INTO resources (title, category, content) VALUES
('Gratitude Practice', 'Positive Psychology', 'Write down 3 things you are grateful for each day. This simple practice can improve mood and outlook.'),
('Strengths Identification', 'Positive Psychology', 'Identify your personal strengths and find ways to use them daily. Visit viacharacter.org for a free assessment.'),
('Acts of Kindness', 'Positive Psychology', 'Helping others boosts your own well-being. Small acts of kindness create positive ripple effects.'),
('Savoring Positive Moments', 'Positive Psychology', 'Pause to fully experience positive moments. Share them with others and reflect on them later.');

SELECT '--- Sample resources inserted successfully! ---' AS message;
SELECT COUNT(*) AS total_resources FROM resources;
