-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 22, 2025 alle 22:34
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pwtriptales_db`
--
CREATE DATABASE IF NOT EXISTS `pwtriptales_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `pwtriptales_db`;

-- --------------------------------------------------------

--
-- Struttura della tabella `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `auth_permission`
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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Token', 6, 'add_token'),
(22, 'Can change Token', 6, 'change_token'),
(23, 'Can delete Token', 6, 'delete_token'),
(24, 'Can view Token', 6, 'view_token'),
(25, 'Can add Token', 7, 'add_tokenproxy'),
(26, 'Can change Token', 7, 'change_tokenproxy'),
(27, 'Can delete Token', 7, 'delete_tokenproxy'),
(28, 'Can view Token', 7, 'view_tokenproxy'),
(29, 'Can add custom user', 8, 'add_customuser'),
(30, 'Can change custom user', 8, 'change_customuser'),
(31, 'Can delete custom user', 8, 'delete_customuser'),
(32, 'Can view custom user', 8, 'view_customuser'),
(33, 'Can add trip group', 9, 'add_tripgroup'),
(34, 'Can change trip group', 9, 'change_tripgroup'),
(35, 'Can delete trip group', 9, 'delete_tripgroup'),
(36, 'Can view trip group', 9, 'view_tripgroup'),
(37, 'Can add badge', 10, 'add_badge'),
(38, 'Can change badge', 10, 'change_badge'),
(39, 'Can delete badge', 10, 'delete_badge'),
(40, 'Can view badge', 10, 'view_badge'),
(41, 'Can add user group badge', 11, 'add_usergroupbadge'),
(42, 'Can change user group badge', 11, 'change_usergroupbadge'),
(43, 'Can delete user group badge', 11, 'delete_usergroupbadge'),
(44, 'Can view user group badge', 11, 'view_usergroupbadge'),
(45, 'Can add image', 12, 'add_image'),
(46, 'Can change image', 12, 'change_image'),
(47, 'Can delete image', 12, 'delete_image'),
(48, 'Can view image', 12, 'view_image'),
(49, 'Can add post', 13, 'add_post'),
(50, 'Can change post', 13, 'change_post'),
(51, 'Can delete post', 13, 'delete_post'),
(52, 'Can view post', 13, 'view_post'),
(53, 'Can add comment', 14, 'add_comment'),
(54, 'Can change comment', 14, 'change_comment'),
(55, 'Can delete comment', 14, 'delete_comment'),
(56, 'Can view comment', 14, 'view_comment');

-- --------------------------------------------------------

--
-- Struttura della tabella `comments_comment`
--

CREATE TABLE `comments_comment` (
  `id` bigint(20) NOT NULL,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `author_id` bigint(20) DEFAULT NULL,
  `post_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `customuser`
--

CREATE TABLE `customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `bio` longtext DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `customuser_groups`
--

CREATE TABLE `customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `customuser_user_permissions`
--

CREATE TABLE `customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'authtoken', 'token'),
(7, 'authtoken', 'tokenproxy'),
(14, 'comments', 'comment'),
(4, 'contenttypes', 'contenttype'),
(12, 'images', 'image'),
(13, 'posts', 'post'),
(5, 'sessions', 'session'),
(10, 'trips', 'badge'),
(9, 'trips', 'tripgroup'),
(11, 'trips', 'usergroupbadge'),
(8, 'users', 'customuser');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-05-22 20:33:31.942766'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-05-22 20:33:31.987960'),
(3, 'auth', '0001_initial', '2025-05-22 20:33:32.170669'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-05-22 20:33:32.206964'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-05-22 20:33:32.213108'),
(6, 'auth', '0004_alter_user_username_opts', '2025-05-22 20:33:32.219846'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-05-22 20:33:32.225684'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-05-22 20:33:32.228258'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-05-22 20:33:32.233881'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-05-22 20:33:32.240078'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-05-22 20:33:32.245784'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-05-22 20:33:32.255939'),
(13, 'auth', '0011_update_proxy_permissions', '2025-05-22 20:33:32.263900'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-05-22 20:33:32.273356'),
(15, 'users', '0001_initial', '2025-05-22 20:33:32.505766'),
(16, 'admin', '0001_initial', '2025-05-22 20:33:32.596338'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-05-22 20:33:32.604872'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-05-22 20:33:32.613565'),
(19, 'authtoken', '0001_initial', '2025-05-22 20:33:32.665979'),
(20, 'authtoken', '0002_auto_20160226_1747', '2025-05-22 20:33:32.691940'),
(21, 'authtoken', '0003_tokenproxy', '2025-05-22 20:33:32.695869'),
(22, 'authtoken', '0004_alter_tokenproxy_options', '2025-05-22 20:33:32.702285'),
(23, 'images', '0001_initial', '2025-05-22 20:33:32.756872'),
(24, 'images', '0002_image_latitude_image_longitude', '2025-05-22 20:33:32.791395'),
(25, 'posts', '0001_initial', '2025-05-22 20:33:32.969673'),
(26, 'comments', '0001_initial', '2025-05-22 20:33:33.063429'),
(27, 'trips', '0001_initial', '2025-05-22 20:33:33.205095'),
(28, 'posts', '0002_post_group', '2025-05-22 20:33:33.255312'),
(29, 'sessions', '0001_initial', '2025-05-22 20:33:33.278508'),
(30, 'trips', '0002_badge_usergroupbadge', '2025-05-22 20:33:33.508772'),
(31, 'users', '0002_alter_customuser_options_alter_customuser_table', '2025-05-22 20:33:33.568883');

-- --------------------------------------------------------

--
-- Struttura della tabella `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `images_image`
--

CREATE TABLE `images_image` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `posts_post`
--

CREATE TABLE `posts_post` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) DEFAULT NULL,
  `image_id` bigint(20) DEFAULT NULL,
  `group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `posts_post_likes`
--

CREATE TABLE `posts_post_likes` (
  `id` bigint(20) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `trips_badge`
--

CREATE TABLE `trips_badge` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `trips_tripgroup`
--

CREATE TABLE `trips_tripgroup` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `trips_tripgroup_members`
--

CREATE TABLE `trips_tripgroup_members` (
  `id` bigint(20) NOT NULL,
  `tripgroup_id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `trips_usergroupbadge`
--

CREATE TABLE `trips_usergroupbadge` (
  `id` bigint(20) NOT NULL,
  `date_awarded` datetime(6) NOT NULL,
  `badge_id` bigint(20) NOT NULL,
  `group_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indici per le tabelle `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indici per le tabelle `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indici per le tabelle `comments_comment`
--
ALTER TABLE `comments_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `comments_comment_author_id_334ce9e2_fk_users_customuser_id` (`author_id`),
  ADD KEY `comments_comment_post_id_96a9ac05_fk_posts_post_id` (`post_id`);

--
-- Indici per le tabelle `customuser`
--
ALTER TABLE `customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indici per le tabelle `customuser_groups`
--
ALTER TABLE `customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`);

--
-- Indici per le tabelle `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`);

--
-- Indici per le tabelle `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`);

--
-- Indici per le tabelle `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indici per le tabelle `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indici per le tabelle `images_image`
--
ALTER TABLE `images_image`
  ADD PRIMARY KEY (`id`),
  ADD KEY `images_image_created_by_id_176f17ff_fk_users_customuser_id` (`created_by_id`);

--
-- Indici per le tabelle `posts_post`
--
ALTER TABLE `posts_post`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `posts_post_created_by_id_2e5f1620_fk_users_customuser_id` (`created_by_id`),
  ADD KEY `posts_post_image_id_e1ecdfd3_fk_images_image_id` (`image_id`),
  ADD KEY `posts_post_group_id_c91a8485_fk_trips_tripgroup_id` (`group_id`);

--
-- Indici per le tabelle `posts_post_likes`
--
ALTER TABLE `posts_post_likes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `posts_post_likes_post_id_customuser_id_0fe642f9_uniq` (`post_id`,`customuser_id`),
  ADD KEY `posts_post_likes_customuser_id_3d64be90_fk_users_customuser_id` (`customuser_id`);

--
-- Indici per le tabelle `trips_badge`
--
ALTER TABLE `trips_badge`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indici per le tabelle `trips_tripgroup`
--
ALTER TABLE `trips_tripgroup`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `trips_tripgroup_created_by_id_dd031340_fk_users_customuser_id` (`created_by_id`);

--
-- Indici per le tabelle `trips_tripgroup_members`
--
ALTER TABLE `trips_tripgroup_members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `trips_tripgroup_members_tripgroup_id_customuser_id_68cc89ea_uniq` (`tripgroup_id`,`customuser_id`),
  ADD KEY `trips_tripgroup_memb_customuser_id_027ef921_fk_users_cus` (`customuser_id`);

--
-- Indici per le tabelle `trips_usergroupbadge`
--
ALTER TABLE `trips_usergroupbadge`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `trips_usergroupbadge_user_id_group_id_10dc1878_uniq` (`user_id`,`group_id`),
  ADD KEY `trips_usergroupbadge_badge_id_ff917403_fk_trips_badge_id` (`badge_id`),
  ADD KEY `trips_usergroupbadge_group_id_c4702971_fk_trips_tripgroup_id` (`group_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT per la tabella `comments_comment`
--
ALTER TABLE `comments_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `customuser`
--
ALTER TABLE `customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `customuser_groups`
--
ALTER TABLE `customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT per la tabella `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT per la tabella `images_image`
--
ALTER TABLE `images_image`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `posts_post`
--
ALTER TABLE `posts_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `posts_post_likes`
--
ALTER TABLE `posts_post_likes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `trips_badge`
--
ALTER TABLE `trips_badge`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `trips_tripgroup`
--
ALTER TABLE `trips_tripgroup`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `trips_tripgroup_members`
--
ALTER TABLE `trips_tripgroup_members`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `trips_usergroupbadge`
--
ALTER TABLE `trips_usergroupbadge`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `customuser` (`id`);

--
-- Limiti per la tabella `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Limiti per la tabella `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Limiti per la tabella `comments_comment`
--
ALTER TABLE `comments_comment`
  ADD CONSTRAINT `comments_comment_author_id_334ce9e2_fk_users_customuser_id` FOREIGN KEY (`author_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `comments_comment_post_id_96a9ac05_fk_posts_post_id` FOREIGN KEY (`post_id`) REFERENCES `posts_post` (`id`);

--
-- Limiti per la tabella `customuser_groups`
--
ALTER TABLE `customuser_groups`
  ADD CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Limiti per la tabella `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  ADD CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Limiti per la tabella `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `customuser` (`id`);

--
-- Limiti per la tabella `images_image`
--
ALTER TABLE `images_image`
  ADD CONSTRAINT `images_image_created_by_id_176f17ff_fk_users_customuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `customuser` (`id`);

--
-- Limiti per la tabella `posts_post`
--
ALTER TABLE `posts_post`
  ADD CONSTRAINT `posts_post_created_by_id_2e5f1620_fk_users_customuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `posts_post_group_id_c91a8485_fk_trips_tripgroup_id` FOREIGN KEY (`group_id`) REFERENCES `trips_tripgroup` (`id`),
  ADD CONSTRAINT `posts_post_image_id_e1ecdfd3_fk_images_image_id` FOREIGN KEY (`image_id`) REFERENCES `images_image` (`id`);

--
-- Limiti per la tabella `posts_post_likes`
--
ALTER TABLE `posts_post_likes`
  ADD CONSTRAINT `posts_post_likes_customuser_id_3d64be90_fk_users_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `posts_post_likes_post_id_7f646a71_fk_posts_post_id` FOREIGN KEY (`post_id`) REFERENCES `posts_post` (`id`);

--
-- Limiti per la tabella `trips_tripgroup`
--
ALTER TABLE `trips_tripgroup`
  ADD CONSTRAINT `trips_tripgroup_created_by_id_dd031340_fk_users_customuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `customuser` (`id`);

--
-- Limiti per la tabella `trips_tripgroup_members`
--
ALTER TABLE `trips_tripgroup_members`
  ADD CONSTRAINT `trips_tripgroup_memb_customuser_id_027ef921_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `trips_tripgroup_memb_tripgroup_id_a62feffc_fk_trips_tri` FOREIGN KEY (`tripgroup_id`) REFERENCES `trips_tripgroup` (`id`);

--
-- Limiti per la tabella `trips_usergroupbadge`
--
ALTER TABLE `trips_usergroupbadge`
  ADD CONSTRAINT `trips_usergroupbadge_badge_id_ff917403_fk_trips_badge_id` FOREIGN KEY (`badge_id`) REFERENCES `trips_badge` (`id`),
  ADD CONSTRAINT `trips_usergroupbadge_group_id_c4702971_fk_trips_tripgroup_id` FOREIGN KEY (`group_id`) REFERENCES `trips_tripgroup` (`id`),
  ADD CONSTRAINT `trips_usergroupbadge_user_id_8c64dbc9_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `customuser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
