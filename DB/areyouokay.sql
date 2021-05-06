-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2021 at 07:19 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `areyouokay`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_artikel`
--

CREATE TABLE `app_artikel` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `createdBy_id` int(11) NOT NULL,
  `isi` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_artikel`
--

INSERT INTO `app_artikel` (`id`, `judul`, `cover`, `createdAt`, `createdBy_id`, `isi`) VALUES
(1, 'Apa itu Depresi?', 'jndejndjdn', '2021-05-06 11:44:04.000000', 2, '');

-- --------------------------------------------------------

--
-- Table structure for table `app_hasildeteksi`
--

CREATE TABLE `app_hasildeteksi` (
  `id` int(11) NOT NULL,
  `hasil_hitung` double NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `pengguna_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_hasildeteksi`
--

INSERT INTO `app_hasildeteksi` (`id`, `hasil_hitung`, `createdAt`, `pengguna_id`) VALUES
(1, 456, '2021-05-06 11:39:26.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_historypertanyaanjawaban`
--

CREATE TABLE `app_historypertanyaanjawaban` (
  `id` int(11) NOT NULL,
  `HasilDeteksi_id` int(11) NOT NULL,
  `Jawaban_id` int(11) NOT NULL,
  `Pertanyaan_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_historypertanyaanjawaban`
--

INSERT INTO `app_historypertanyaanjawaban` (`id`, `HasilDeteksi_id`, `Jawaban_id`, `Pertanyaan_id`) VALUES
(1, 1, 1, 21);

-- --------------------------------------------------------

--
-- Table structure for table `app_jawaban`
--

CREATE TABLE `app_jawaban` (
  `id` int(11) NOT NULL,
  `jawaban` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_jawaban`
--

INSERT INTO `app_jawaban` (`id`, `jawaban`) VALUES
(1, 'Sangat Sesuai'),
(2, 'Sesuai'),
(3, 'Netral'),
(4, 'Tidak Sesuai'),
(5, 'Sangat Tidak Sesuai');

-- --------------------------------------------------------

--
-- Table structure for table `app_penanganan`
--

CREATE TABLE `app_penanganan` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `createdBy_id` int(11) NOT NULL,
  `tingkat_depresi_id` int(11) NOT NULL,
  `isi` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_penanganan`
--

INSERT INTO `app_penanganan` (`id`, `judul`, `cover`, `createdAt`, `createdBy_id`, `tingkat_depresi_id`, `isi`) VALUES
(1, 'Self Love', 'nbhhbdwhbd', '2021-05-06 11:40:07.000000', 1, 4, '');

-- --------------------------------------------------------

--
-- Table structure for table `app_pencegahan`
--

CREATE TABLE `app_pencegahan` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `createdBy_id` int(11) NOT NULL,
  `isi` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_pencegahan`
--

INSERT INTO `app_pencegahan` (`id`, `judul`, `cover`, `createdAt`, `createdBy_id`, `isi`) VALUES
(1, 'Baca Buku', 'dhbnhj', '2021-05-06 11:43:41.000000', 2, '');

-- --------------------------------------------------------

--
-- Table structure for table `app_pengguna`
--

CREATE TABLE `app_pengguna` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `ttl` date NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `pekerjaan` varchar(255) NOT NULL,
  `createdAt` datetime(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_pengguna`
--

INSERT INTO `app_pengguna` (`id`, `nama`, `email`, `ttl`, `jenis_kelamin`, `pekerjaan`, `createdAt`) VALUES
(1, 'Nurul Amala Azza', 'mala@gmail.com', '1999-05-05', 'Perempuan', 'Mahasiswa', '2021-05-06 10:01:04.000000'),
(2, 'Ufairoh Nabihah', 'ufa@gmail.com', '1999-05-01', 'Perempuan', 'Mahasiswa', '2021-05-02 10:01:50.000000');

-- --------------------------------------------------------

--
-- Table structure for table `app_pertanyaan`
--

CREATE TABLE `app_pertanyaan` (
  `id` int(11) NOT NULL,
  `pertanyaan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_pertanyaan`
--

INSERT INTO `app_pertanyaan` (`id`, `pertanyaan`) VALUES
(1, 'Saya merasa sedih selama dua minggu terakhir'),
(2, 'Saya merasa pesimis selama dua minggu terakhir'),
(3, 'Saya merasa lebih gagal dari orang lain selama dua minggu terakhir'),
(4, 'Saya kehilangan kesenangan selama dua minggu terakhir'),
(5, 'Saya merasa bersalah selama dua minggu terakhir'),
(6, 'Saya merasa saya akan dihukum selama dua minggu terakhir'),
(7, 'Saya tidak menyukai diri saya sendiri selama dua minggu terakhir'),
(8, 'Saya suka mengkritik diri sendiri selama dua minggu terakhir'),
(9, 'Saya memiliki keinginan untuk bunuh diri selama dua minggu terakhir'),
(10, 'Saya lebih sering menangis selama dua minggu terakhir'),
(11, 'Saya merasa gelisah selama dua minggu terakhir'),
(12, 'Saya merasa kehilangan minat pada kegiatan yang dulu saya gemari '),
(13, 'Saya sulit mengambil keputusan selama dua minggu terakhir'),
(14, 'Saya merasa tidak berharga dan tidak berdaya selama dua minggu terakhir'),
(15, 'Saya merasa kehilangan energi selama dua minggu terakhir'),
(16, 'Terdapat perubahan dalam pola tidur saya selama dua minggu terakhir'),
(17, 'Saya mudah tersinggung selama dua minggu terakhir'),
(18, 'Saya mengalami perubahan dalam selera makan selama dua minggu terakhir'),
(19, 'Saya sulit berkonsentrasi selama dua minggu terakhir'),
(20, 'Saya merasa cepat lelah selama dua minggu terakhir'),
(21, 'Saya kehilangan minat dalam melakukan hubungan seksual selama dua minggu terakhir');

-- --------------------------------------------------------

--
-- Table structure for table `app_tingkatdepresi`
--

CREATE TABLE `app_tingkatdepresi` (
  `id` int(11) NOT NULL,
  `nama_depresi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tingkatdepresi`
--

INSERT INTO `app_tingkatdepresi` (`id`, `nama_depresi`) VALUES
(1, 'Tidak Depresi'),
(2, 'Depresi Ringan'),
(3, 'Depresi Sedang'),
(4, 'Depresi Berat');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add dashboard', 7, 'add_dashboard'),
(26, 'Can change dashboard', 7, 'change_dashboard'),
(27, 'Can delete dashboard', 7, 'delete_dashboard'),
(28, 'Can view dashboard', 7, 'view_dashboard'),
(29, 'Can add hasil deteksi', 8, 'add_hasildeteksi'),
(30, 'Can change hasil deteksi', 8, 'change_hasildeteksi'),
(31, 'Can delete hasil deteksi', 8, 'delete_hasildeteksi'),
(32, 'Can view hasil deteksi', 8, 'view_hasildeteksi'),
(33, 'Can add pengguna', 9, 'add_pengguna'),
(34, 'Can change pengguna', 9, 'change_pengguna'),
(35, 'Can delete pengguna', 9, 'delete_pengguna'),
(36, 'Can view pengguna', 9, 'view_pengguna'),
(37, 'Can add artikel', 10, 'add_artikel'),
(38, 'Can change artikel', 10, 'change_artikel'),
(39, 'Can delete artikel', 10, 'delete_artikel'),
(40, 'Can view artikel', 10, 'view_artikel'),
(41, 'Can add penanganan', 11, 'add_penanganan'),
(42, 'Can change penanganan', 11, 'change_penanganan'),
(43, 'Can delete penanganan', 11, 'delete_penanganan'),
(44, 'Can view penanganan', 11, 'view_penanganan'),
(45, 'Can add tingkat depresi', 12, 'add_tingkatdepresi'),
(46, 'Can change tingkat depresi', 12, 'change_tingkatdepresi'),
(47, 'Can delete tingkat depresi', 12, 'delete_tingkatdepresi'),
(48, 'Can view tingkat depresi', 12, 'view_tingkatdepresi'),
(49, 'Can add pencegahan', 13, 'add_pencegahan'),
(50, 'Can change pencegahan', 13, 'change_pencegahan'),
(51, 'Can delete pencegahan', 13, 'delete_pencegahan'),
(52, 'Can view pencegahan', 13, 'view_pencegahan'),
(53, 'Can add jawaban', 14, 'add_jawaban'),
(54, 'Can change jawaban', 14, 'change_jawaban'),
(55, 'Can delete jawaban', 14, 'delete_jawaban'),
(56, 'Can view jawaban', 14, 'view_jawaban'),
(57, 'Can add history pertanyaan jawaban', 15, 'add_historypertanyaanjawaban'),
(58, 'Can change history pertanyaan jawaban', 15, 'change_historypertanyaanjawaban'),
(59, 'Can delete history pertanyaan jawaban', 15, 'delete_historypertanyaanjawaban'),
(60, 'Can view history pertanyaan jawaban', 15, 'view_historypertanyaanjawaban'),
(61, 'Can add pertanyaan', 16, 'add_pertanyaan'),
(62, 'Can change pertanyaan', 16, 'change_pertanyaan'),
(63, 'Can delete pertanyaan', 16, 'delete_pertanyaan'),
(64, 'Can view pertanyaan', 16, 'view_pertanyaan');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$zhyMlS5ft3yJ$VKYPndUUQKS43XdELCNfPJUY5EtWUctjM70PK0wMNw4=', '2021-05-04 23:07:24.488673', 1, 'goldenpad', '', '', 'goldenpad.app@gmail.com', 1, 1, '2021-05-04 23:07:14.352909'),
(2, 'pbkdf2_sha256$260000$3rLaMAtwP8cjFUH4u12371$WGz1u9uYbM8Xn75+atcsCJd3oLSsaeiVw4mq/yShs2g=', NULL, 1, 'joko', '', '', 'goldenpad.app@gmail.com', 1, 1, '2021-05-06 01:18:15.941005');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_dashboard`
--

CREATE TABLE `dashboard_dashboard` (
  `id` bigint(20) NOT NULL,
  `tanggal` datetime(6) NOT NULL,
  `hasil_hitung` double NOT NULL,
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'app', 'artikel'),
(8, 'app', 'hasildeteksi'),
(15, 'app', 'historypertanyaanjawaban'),
(14, 'app', 'jawaban'),
(11, 'app', 'penanganan'),
(13, 'app', 'pencegahan'),
(9, 'app', 'pengguna'),
(16, 'app', 'pertanyaan'),
(12, 'app', 'tingkatdepresi'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'dashboard', 'dashboard'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-04 23:05:50.668778'),
(2, 'auth', '0001_initial', '2021-05-04 23:05:52.993514'),
(3, 'admin', '0001_initial', '2021-05-04 23:06:05.057951'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-04 23:06:08.708146'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-04 23:06:08.770399'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-05-04 23:06:09.631606'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-05-04 23:06:11.316004'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-05-04 23:06:11.617625'),
(9, 'auth', '0004_alter_user_username_opts', '2021-05-04 23:06:11.730106'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-05-04 23:06:12.573787'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-05-04 23:06:12.628677'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-04 23:06:12.773450'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-05-04 23:06:13.008126'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-04 23:06:13.247993'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-05-04 23:06:13.570497'),
(16, 'auth', '0011_update_proxy_permissions', '2021-05-04 23:06:13.705849'),
(17, 'sessions', '0001_initial', '2021-05-04 23:06:14.264740'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-05-06 01:18:46.483150'),
(19, 'dashboard', '0001_initial', '2021-05-06 02:00:11.517947'),
(20, 'app', '0001_initial', '2021-05-06 02:50:06.944270'),
(21, 'app', '0002_auto_20210506_1148', '2021-05-06 04:48:39.387199'),
(22, 'app', '0003_historypertanyaanjawaban_jawaban_pertanyaan', '2021-05-06 05:02:27.495061');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7kgw43ey29rmkqsaq04287k86a4au11o', 'ZTA2ZDA1NWMyMmQxNzQ5NTU4MTRiZWRlMDEwM2U5MzA4ZDYyNGI4ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNGViYTY0MTM1NjA3NDhkN2YzYjhhNzJjNjhmOGY4ODg5N2UwZTM2In0=', '2021-05-18 23:07:24.540473');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_artikel`
--
ALTER TABLE `app_artikel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_artikel_createdBy_id_505607dc_fk_auth_user_id` (`createdBy_id`);

--
-- Indexes for table `app_hasildeteksi`
--
ALTER TABLE `app_hasildeteksi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_hasildeteksi_pengguna_id_90249924_fk_app_pengguna_id` (`pengguna_id`);

--
-- Indexes for table `app_historypertanyaanjawaban`
--
ALTER TABLE `app_historypertanyaanjawaban`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_historypertanyaa_HasilDeteksi_id_95ac808e_fk_app_hasil` (`HasilDeteksi_id`),
  ADD KEY `app_historypertanyaa_Jawaban_id_6df33bde_fk_app_jawab` (`Jawaban_id`),
  ADD KEY `app_historypertanyaa_Pertanyaan_id_3acef1bb_fk_app_perta` (`Pertanyaan_id`);

--
-- Indexes for table `app_jawaban`
--
ALTER TABLE `app_jawaban`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_penanganan`
--
ALTER TABLE `app_penanganan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_penanganan_createdBy_id_f132cc76_fk_auth_user_id` (`createdBy_id`),
  ADD KEY `app_penanganan_tingkat_depresi_id_c293013c_fk_app_tingk` (`tingkat_depresi_id`);

--
-- Indexes for table `app_pencegahan`
--
ALTER TABLE `app_pencegahan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_pencegahan_createdBy_id_a9201ff1_fk_auth_user_id` (`createdBy_id`);

--
-- Indexes for table `app_pengguna`
--
ALTER TABLE `app_pengguna`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_pertanyaan`
--
ALTER TABLE `app_pertanyaan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_tingkatdepresi`
--
ALTER TABLE `app_tingkatdepresi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `dashboard_dashboard`
--
ALTER TABLE `dashboard_dashboard`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_artikel`
--
ALTER TABLE `app_artikel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_hasildeteksi`
--
ALTER TABLE `app_hasildeteksi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_historypertanyaanjawaban`
--
ALTER TABLE `app_historypertanyaanjawaban`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_jawaban`
--
ALTER TABLE `app_jawaban`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `app_penanganan`
--
ALTER TABLE `app_penanganan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_pencegahan`
--
ALTER TABLE `app_pencegahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_pengguna`
--
ALTER TABLE `app_pengguna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_pertanyaan`
--
ALTER TABLE `app_pertanyaan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `app_tingkatdepresi`
--
ALTER TABLE `app_tingkatdepresi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dashboard_dashboard`
--
ALTER TABLE `dashboard_dashboard`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_artikel`
--
ALTER TABLE `app_artikel`
  ADD CONSTRAINT `app_artikel_createdBy_id_505607dc_fk_auth_user_id` FOREIGN KEY (`createdBy_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_hasildeteksi`
--
ALTER TABLE `app_hasildeteksi`
  ADD CONSTRAINT `app_hasildeteksi_pengguna_id_90249924_fk_app_pengguna_id` FOREIGN KEY (`pengguna_id`) REFERENCES `app_pengguna` (`id`);

--
-- Constraints for table `app_historypertanyaanjawaban`
--
ALTER TABLE `app_historypertanyaanjawaban`
  ADD CONSTRAINT `app_historypertanyaa_HasilDeteksi_id_95ac808e_fk_app_hasil` FOREIGN KEY (`HasilDeteksi_id`) REFERENCES `app_hasildeteksi` (`id`),
  ADD CONSTRAINT `app_historypertanyaa_Jawaban_id_6df33bde_fk_app_jawab` FOREIGN KEY (`Jawaban_id`) REFERENCES `app_jawaban` (`id`),
  ADD CONSTRAINT `app_historypertanyaa_Pertanyaan_id_3acef1bb_fk_app_perta` FOREIGN KEY (`Pertanyaan_id`) REFERENCES `app_pertanyaan` (`id`);

--
-- Constraints for table `app_penanganan`
--
ALTER TABLE `app_penanganan`
  ADD CONSTRAINT `app_penanganan_createdBy_id_f132cc76_fk_auth_user_id` FOREIGN KEY (`createdBy_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `app_penanganan_tingkat_depresi_id_c293013c_fk_app_tingk` FOREIGN KEY (`tingkat_depresi_id`) REFERENCES `app_tingkatdepresi` (`id`);

--
-- Constraints for table `app_pencegahan`
--
ALTER TABLE `app_pencegahan`
  ADD CONSTRAINT `app_pencegahan_createdBy_id_a9201ff1_fk_auth_user_id` FOREIGN KEY (`createdBy_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
