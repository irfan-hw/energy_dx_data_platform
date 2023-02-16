-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- ホスト: db
-- 生成日時: 2022 年 12 月 28 日 00:41
-- サーバのバージョン： 8.0.27
-- PHP のバージョン: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `edx_controller`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `t_controller`
--

CREATE TABLE `t_controller` (
  `controller_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'システム全体で一意',
  `server_uri` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[setting] ThingsBoard API',
  `server_accesstoken` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[setting] ThingsBoard API',
  `server_access_interval` int NOT NULL COMMENT '[setting] 秒で指定',
  `last_server_access` datetime NOT NULL COMMENT '[status] 前回サーバーアクセス日時',
  `next_server_access` datetime NOT NULL COMMENT '[status] 次回サーバーアクセス日時',
  `status` tinyint NOT NULL COMMENT '[status] 正常or異常',
  `active` tinyint(1) NOT NULL COMMENT '[status] 稼働中or休止中',
  `last_server_sync` datetime DEFAULT NULL COMMENT '[status] サーバー同期最終日時',
  `version` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[status] コントローラーアプリバージョン',
  `last_updated` datetime NOT NULL COMMENT '[other] アプリ最終更新日時'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='コントローラー管理(GW設定)';

-- --------------------------------------------------------

--
-- テーブルの構造 `t_data_get`
--

CREATE TABLE `t_data_get` (
  `device_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[FK] device.device_id',
  `get_cd` smallint NOT NULL COMMENT '[FK] protocol_ecl',
  `datetime_start` datetime NOT NULL COMMENT '例)YYYYMMDD 00:00:00 ※30分単位の場合',
  `datetime_end` datetime NOT NULL COMMENT '例)YYYYMMDD 00:29:59 ※30分単位の場合',
  `value` binary(16) NOT NULL COMMENT '値',
  `server_sync` tinyint(1) NOT NULL COMMENT 'サーバー未同期:0,同期済:1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='デバイス取得データ (計測値/状態値)';

-- --------------------------------------------------------

--
-- テーブルの構造 `t_data_set`
--

CREATE TABLE `t_data_set` (
  `device_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[FK] device.device_id',
  `set_cd` smallint NOT NULL COMMENT '[FK] protocol_ecl',
  `datetime` datetime NOT NULL COMMENT '設定値を反映するタイミング',
  `plan_no` mediumint NOT NULL COMMENT '再計画でアップする No.',
  `value` binary(16) NOT NULL COMMENT '値',
  `device_sync` tinyint(1) NOT NULL COMMENT 'デバイス未反映:0,反映済:1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='デバイス更新データ (制御値/設定値)';

-- --------------------------------------------------------

--
-- テーブルの構造 `t_devices`
--

CREATE TABLE `t_devices` (
  `device_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'コントローラーで一意',
  `device_type` smallint NOT NULL COMMENT '[info] (FK) sys_device_type システムで定義されるタイプ',
  `device_info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '[info] ノードプロファイルを想定 ※複数フィールドの可能性あり',
  `address_IPv6` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[info]',
  `address_IPv4` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[info]',
  `protocol` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '[info] 利用するプロトコル振り分け用 ECHPNET Lite:"01",DI:"11",DO:"21"',
  `access_get_interval` int NOT NULL COMMENT '[setting] GET(計測・状態取得)インターバル ※秒指定',
  `access_set_interval` int NOT NULL COMMENT '[setting] SET(設定変更)インターバル ※秒指定',
  `last_access_get` datetime NOT NULL COMMENT '[status] 前回アクセス日時(GET)',
  `last_access_set` datetime NOT NULL COMMENT '[status] 前回アクセス日時(SET)',
  `next_access_get` datetime NOT NULL COMMENT '[status] 次回アクセス日時(GET)',
  `next_access_set` datetime NOT NULL COMMENT '[status] 次回アクセス日時(SET)',
  `status` smallint NOT NULL COMMENT '[status] 正常or異常',
  `active` tinyint NOT NULL COMMENT '[status] 利用中or休止中',
  `server_sync` smallint NOT NULL COMMENT '[status] サーバー未同期:0,追加済:1,更新済:2,更新失敗:-1',
  `last_server_sync` datetime DEFAULT NULL COMMENT '[status] 最終サーバー同期日時',
  `added` datetime NOT NULL COMMENT '[other] コントローラーに追加された日時',
  `deleted` datetime DEFAULT NULL COMMENT '[other] コントローラーから削除された日時'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='デバイス管理';

-- --------------------------------------------------------

--
-- テーブルの構造 `t_device_DIDO`
--

CREATE TABLE `t_device_DIDO` (
  `id` int NOT NULL COMMENT 'INDEX',
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '例) WHM.積算電力量',
  `sys_device_type` smallint NOT NULL COMMENT '例) WHM:101 -> devices.device_type',
  `sys_di_or_do` tinyint(1) NOT NULL COMMENT 'DI:0,DO:1\r\n\r\n',
  `sys_di_or_do_cd` smallint NOT NULL COMMENT 'sys_device_type で一意'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='デバイスマスタ DIDO';

-- --------------------------------------------------------

--
-- テーブルの構造 `t_device_ENL`
--

CREATE TABLE `t_device_ENL` (
  `id` int NOT NULL COMMENT 'INDEX',
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'クラス+プロパティ名',
  `sys_device_type` smallint NOT NULL COMMENT 'devices.device_type',
  `sys_get_or_set` tinyint(1) NOT NULL COMMENT 'get:0,set:1',
  `sys_get_or_set_cd` smallint NOT NULL COMMENT 'sys_device_type で一意',
  `ecl_classgroup_cd` binary(1) NOT NULL COMMENT '[ECHONET Lite] クラスグループコード',
  `ecl_class_cd` binary(1) NOT NULL COMMENT '[ECHONET Lite] クラスコード',
  `ecl_EPC` smallint NOT NULL COMMENT '[ECHONET Lite] プロパティコード'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='デバイスプロパティマスタ ECHONET Lite';

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `t_controller`
--
ALTER TABLE `t_controller`
  ADD PRIMARY KEY (`controller_id`);

--
-- テーブルのインデックス `t_data_get`
--
ALTER TABLE `t_data_get`
  ADD PRIMARY KEY (`device_id`,`get_cd`,`datetime_start`);

--
-- テーブルのインデックス `t_data_set`
--
ALTER TABLE `t_data_set`
  ADD PRIMARY KEY (`device_id`,`set_cd`,`datetime`,`plan_no`);

--
-- テーブルのインデックス `t_devices`
--
ALTER TABLE `t_devices`
  ADD PRIMARY KEY (`device_id`);

--
-- テーブルのインデックス `t_device_DIDO`
--
ALTER TABLE `t_device_DIDO`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sys_device_type` (`sys_device_type`,`sys_di_or_do_cd`);

--
-- テーブルのインデックス `t_device_ENL`
--
ALTER TABLE `t_device_ENL`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sys_device_type` (`sys_device_type`,`sys_get_or_set_cd`);

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `t_data_set`
--
ALTER TABLE `t_data_set`
  ADD CONSTRAINT `t_data_set_ibfk_1` FOREIGN KEY (`device_id`) REFERENCES `t_devices` (`device_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- テーブルの制約 `t_devices`
--
ALTER TABLE `t_devices`
  ADD CONSTRAINT `t_devices_ibfk_1` FOREIGN KEY (`device_id`) REFERENCES `t_data_get` (`device_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
