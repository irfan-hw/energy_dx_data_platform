-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- ホスト: db
-- 生成日時: 2022 年 11 月 15 日 01:40
-- サーバのバージョン： 8.0.31
-- PHP のバージョン: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `kishou_data`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `area`
--

CREATE TABLE `area` (
  `area_id` int NOT NULL,
  `area_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `area_code` varchar(32) NOT NULL,
  `prec_no` varchar(8) NOT NULL,
  `bloc_no` varchar(8) NOT NULL,
  `note` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- テーブルのデータのダンプ `area`
--

INSERT INTO `area` (`area_id`, `area_name`, `area_code`, `prec_no`, `bloc_no`, `note`, `deleted`) VALUES
(8, '羽田', 'haneda', '44', '0371', NULL, 0),
(38, '水戸市', 'mito', '40', '47629', NULL, 0),
(42, '相模湖', '-', '46', '0387', NULL, 0);

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_forecasted_5min`
--

CREATE TABLE `weather_forecasted_5min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_forecasted_10min`
--

CREATE TABLE `weather_forecasted_10min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_forecasted_15min`
--

CREATE TABLE `weather_forecasted_15min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_forecasted_30min`
--

CREATE TABLE `weather_forecasted_30min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_forecasted_60min`
--

CREATE TABLE `weather_forecasted_60min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_import_control`
--

CREATE TABLE `weather_import_control` (
  `weather_import_id` int NOT NULL,
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `interval_import_measured_data` int NOT NULL COMMENT 'in minutes(m)',
  `interval_import_forecasted_data` int NOT NULL COMMENT 'in minutes(m)',
  `next_exec_import_measured_datetime` datetime NOT NULL,
  `next_exec_import_forecasted_datetime` datetime NOT NULL,
  `last_exec_import_measured_datetime` datetime NOT NULL,
  `last_exec_import_forecasted_datetime` datetime NOT NULL,
  `active` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- テーブルのデータのダンプ `weather_import_control`
--

INSERT INTO `weather_import_control` (`weather_import_id`, `area_id`, `weather_set_id`, `interval_import_measured_data`, `interval_import_forecasted_data`, `next_exec_import_measured_datetime`, `next_exec_import_forecasted_datetime`, `last_exec_import_measured_datetime`, `last_exec_import_forecasted_datetime`, `active`, `deleted`) VALUES
(1, 8, 3, 1440, 360, '2022-10-27 17:56:44', '2022-10-24 05:45:16', '2022-11-09 13:49:44', '2022-11-09 13:49:44', 1, 0),
(7, 38, 4, 1440, 360, '2022-11-08 05:55:57', '2022-11-08 05:55:57', '2022-11-09 13:49:44', '2022-11-09 13:49:44', 1, 0),
(12, 8, 11, 1440, 360, '2022-11-08 06:05:27', '2022-11-08 06:18:27', '2022-11-09 13:49:44', '2022-11-14 13:15:05', 1, 0),
(17, 38, 21, 1440, 360, '2022-11-08 06:38:57', '2022-11-08 06:55:57', '2022-11-09 13:49:45', '2022-11-14 15:36:57', 1, 0);

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_measured_5min`
--

CREATE TABLE `weather_measured_5min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_measured_10min`
--

CREATE TABLE `weather_measured_10min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_measured_15min`
--

CREATE TABLE `weather_measured_15min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_measured_30min`
--

CREATE TABLE `weather_measured_30min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_measured_60min`
--

CREATE TABLE `weather_measured_60min` (
  `area_id` int NOT NULL,
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL,
  `datetime` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_set`
--

CREATE TABLE `weather_set` (
  `weather_set_id` int NOT NULL,
  `URL_forecasted_data` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `URL_measured_data` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `time_gain` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- テーブルのデータのダンプ `weather_set`
--

INSERT INTO `weather_set` (`weather_set_id`, `URL_forecasted_data`, `URL_measured_data`, `time_gain`) VALUES
(3, '-', 'https://www.data.jma.go.jp/obd/stats/etrn/view/10min_a1.php', '10min'),
(4, '-', 'https://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php', '10min'),
(11, 'https://rest.energy-cloud.jp/api/v1/pro-forecasts/', 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php', '60min'),
(21, 'https://rest.energy-cloud.jp/api/v1/pro-forecasts/', 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php', '60min');

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_set_pivot`
--

CREATE TABLE `weather_set_pivot` (
  `weather_set_id` int NOT NULL,
  `weather_type_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- テーブルのデータのダンプ `weather_set_pivot`
--

INSERT INTO `weather_set_pivot` (`weather_set_id`, `weather_type_id`) VALUES
(3, 1),
(3, 2),
(3, 3),
(4, 1),
(4, 2),
(11, 1),
(11, 2),
(11, 3),
(11, 4),
(11, 5),
(21, 1),
(21, 2);

-- --------------------------------------------------------

--
-- テーブルの構造 `weather_type`
--

CREATE TABLE `weather_type` (
  `weather_type_id` int NOT NULL,
  `weather_type_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `unit` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `decimal_places` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- テーブルのデータのダンプ `weather_type`
--

INSERT INTO `weather_type` (`weather_type_id`, `weather_type_name`, `unit`, `decimal_places`) VALUES
(1, '気温', ' ℃ ', 2),
(2, '湿度', '％', 2),
(3, '降水量', 'mm', 2),
(4, '風速', 'm/s', 2),
(5, '風向', '-', 2);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`area_id`);

--
-- テーブルのインデックス `weather_forecasted_5min`
--
ALTER TABLE `weather_forecasted_5min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_forecasted_10min`
--
ALTER TABLE `weather_forecasted_10min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_forecasted_15min`
--
ALTER TABLE `weather_forecasted_15min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_forecasted_30min`
--
ALTER TABLE `weather_forecasted_30min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_forecasted_60min`
--
ALTER TABLE `weather_forecasted_60min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_import_control`
--
ALTER TABLE `weather_import_control`
  ADD PRIMARY KEY (`weather_import_id`),
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`);

--
-- テーブルのインデックス `weather_measured_5min`
--
ALTER TABLE `weather_measured_5min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`),
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_measured_10min`
--
ALTER TABLE `weather_measured_10min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_measured_15min`
--
ALTER TABLE `weather_measured_15min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_measured_30min`
--
ALTER TABLE `weather_measured_30min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_measured_60min`
--
ALTER TABLE `weather_measured_60min`
  ADD PRIMARY KEY (`datetime`,`area_id`,`weather_set_id`,`weather_type_id`) USING BTREE,
  ADD KEY `area_id` (`area_id`),
  ADD KEY `weather_set_id` (`weather_set_id`),
  ADD KEY `weather_type_id` (`weather_type_id`);

--
-- テーブルのインデックス `weather_set`
--
ALTER TABLE `weather_set`
  ADD PRIMARY KEY (`weather_set_id`) USING BTREE;

--
-- テーブルのインデックス `weather_set_pivot`
--
ALTER TABLE `weather_set_pivot`
  ADD PRIMARY KEY (`weather_set_id`,`weather_type_id`),
  ADD KEY `weather_type_id` (`weather_type_id`,`weather_set_id`) USING BTREE;

--
-- テーブルのインデックス `weather_type`
--
ALTER TABLE `weather_type`
  ADD PRIMARY KEY (`weather_type_id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `area`
--
ALTER TABLE `area`
  MODIFY `area_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- テーブルの AUTO_INCREMENT `weather_import_control`
--
ALTER TABLE `weather_import_control`
  MODIFY `weather_import_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- テーブルの AUTO_INCREMENT `weather_set`
--
ALTER TABLE `weather_set`
  MODIFY `weather_set_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- テーブルの AUTO_INCREMENT `weather_type`
--
ALTER TABLE `weather_type`
  MODIFY `weather_type_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `weather_forecasted_5min`
--
ALTER TABLE `weather_forecasted_5min`
  ADD CONSTRAINT `weather_forecasted_5min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_5min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_5min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_forecasted_10min`
--
ALTER TABLE `weather_forecasted_10min`
  ADD CONSTRAINT `weather_forecasted_10min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_10min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_10min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_forecasted_15min`
--
ALTER TABLE `weather_forecasted_15min`
  ADD CONSTRAINT `weather_forecasted_15min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_15min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_15min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_forecasted_30min`
--
ALTER TABLE `weather_forecasted_30min`
  ADD CONSTRAINT `weather_forecasted_30min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_30min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_30min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_forecasted_60min`
--
ALTER TABLE `weather_forecasted_60min`
  ADD CONSTRAINT `weather_forecasted_60min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_60min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_forecasted_60min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_import_control`
--
ALTER TABLE `weather_import_control`
  ADD CONSTRAINT `weather_import_control_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_import_control_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_measured_5min`
--
ALTER TABLE `weather_measured_5min`
  ADD CONSTRAINT `weather_measured_5min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_5min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_5min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_measured_10min`
--
ALTER TABLE `weather_measured_10min`
  ADD CONSTRAINT `weather_measured_10min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_10min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_10min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_measured_15min`
--
ALTER TABLE `weather_measured_15min`
  ADD CONSTRAINT `weather_measured_15min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_15min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_15min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_measured_30min`
--
ALTER TABLE `weather_measured_30min`
  ADD CONSTRAINT `weather_measured_30min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_30min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_30min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_measured_60min`
--
ALTER TABLE `weather_measured_60min`
  ADD CONSTRAINT `weather_measured_60min_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_60min_ibfk_2` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_measured_60min_ibfk_3` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- テーブルの制約 `weather_set_pivot`
--
ALTER TABLE `weather_set_pivot`
  ADD CONSTRAINT `weather_set_pivot_ibfk_1` FOREIGN KEY (`weather_set_id`) REFERENCES `weather_set` (`weather_set_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `weather_set_pivot_ibfk_2` FOREIGN KEY (`weather_type_id`) REFERENCES `weather_type` (`weather_type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
